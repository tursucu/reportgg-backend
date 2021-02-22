import datetime

from typing import Type, TypeVar, MutableMapping, Any, Iterable
from datapipelines import DataSource, DataSink, PipelineContext, Query, validate_query, NotFoundError

from .models import Summoner as MongoSummoner
from .common import MongoBaseObject
from kogmaw.dto.summoner import SummonerDto
from kogmaw.data import Platform, Region
from kogmaw.datastores.uniquekeys import convert_region_to_platform

from mongoengine import *
from mongoengine import DoesNotExist, signals

T = TypeVar("T")

default_expirations = {
    SummonerDto: datetime.timedelta(minutes=1),
}


class Mongo(DataSource, DataSink):
    def __init__(self, expirations: MutableMapping[type, float] = None) -> None:
        self._expirations = dict(expirations) if expirations is not None else default_expirations

        for key, value in list(self._expirations.items()):
            if isinstance(key, str):
                new_key = globals()[key]
                self._expirations[new_key] = self._expirations.pop(key)
                key = new_key
            if value != -1 and isinstance(value, datetime.timedelta):
                self._expirations[key] = value.seconds + 24 * 60 * 60 * value.days

    @DataSource.dispatch
    def get(self, type: Type[T], query: MutableMapping[str, Any], context: PipelineContext = None) -> T:
        pass

    @DataSource.dispatch
    def get_many(self, type: Type[T], query: MutableMapping[str, Any], context: PipelineContext = None) -> Iterable[T]:
        pass

    @DataSink.dispatch
    def put(self, type: Type[T], item: T, context: PipelineContext = None) -> None:
        pass

    @DataSink.dispatch
    def put_many(self, type: Type[T], items: Iterable[T], context: PipelineContext = None) -> None:
        pass

    def _put(self, item: MongoBaseObject):
        if item._dto_type in self._expirations and self._expirations[item._dto_type] == 0:
            # The expiration time has been set to 0 -> shoud not be cached
            return
        item.updated()
        change = {
            "id": item["id"],
            "region": item["region"],
            "accountId": item["accountId"],
            "name": item["name"],
            "profileIconId": item["profileIconId"],
            "puuid": item["puuid"],
            "revisionDate": item["revisionDate"],
            "summonerLevel": item["summonerLevel"],
            "lastUpdate": item["lastUpdate"]
        }
        summoner = MongoSummoner.objects(region=item["region"], id=item["id"])
        summoner.update(**change, upsert=True)

    def _first(self, query):
        try:
            result = query.first()
            if result is None:
                raise NotFoundError
            else:
                if result.has_expired(self._expirations):
                    print("Has Expired Çalıştı! Veri Güncelleniyor.")
                    raise NotFoundError
                print("MongoDB Veri süresi geçerliliği dolmadı. Veri Güncellenmedi.", self._expirations)
                return result


        except DoesNotExist:
            raise NotFoundError

    ################
    # Summoner API #
    ################

    _validate_get_summoner_query = Query. \
        has("id").as_(str). \
        or_("accountId").as_(str). \
        or_("puuid").as_(str). \
        or_("name").as_(str).also. \
        has("platform").as_(Platform)

    @get.register(SummonerDto)
    @validate_query(_validate_get_summoner_query, convert_region_to_platform)
    def get_summoner(self, query: MutableMapping[str, Any], context: PipelineContext = None) -> SummonerDto:
        region_str = query["region"].value

        if "id" in query:
            print("Id Çalıştı")
            summoner = self._first(MongoSummoner.objects(region=region_str, id=query["id"]))
        elif "name" in query:
            print("Name Çalıştı")
            summoner = self._first(MongoSummoner.objects(region=region_str, name=query["name"]))
        elif "accountId" in query:
            summoner = self._first(MongoSummoner.objects(region=region_str, accountId=query["accountId"]))
        elif "puuid" in query:
            summoner = self._first(MongoSummoner.objects(region=region_str, puuid=query["puuid"]))
        else:
            raise RuntimeError("Impossible!")
        return summoner.to_dto()

    @put.register(SummonerDto)
    def put_summoner(self, item: SummonerDto, context: PipelineContext = None) -> None:
        """if "id" in item:
            summoner = MongoSummoner.objects(region=item["region"], id=item["id"])
        summoner.update(**item, upsert=True)"""
        if not "platform" in item:
            item["platform"] = Region(item["region"]).platform.value
        self._put(MongoSummoner(**item))
