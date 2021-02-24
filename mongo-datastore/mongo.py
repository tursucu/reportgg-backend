import datetime

from mongoengine import *
from mongoengine import DoesNotExist

from typing import Type, TypeVar, MutableMapping, Any, Iterable
from datapipelines import DataSource, DataSink, PipelineContext, Query, validate_query, NotFoundError

from .models import Summoner as MongoSummoner, Match as MongoMatch
from .common import MongoBaseObject
from kogmaw.dto.summoner import SummonerDto
from kogmaw.dto.match import MatchDto, TimelineDto
from kogmaw.data import Platform, Region
from kogmaw.datastores.uniquekeys import convert_region_to_platform

T = TypeVar("T")

default_expirations = {
    SummonerDto: datetime.timedelta(minutes=1),
    MatchDto: -1,
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

    #####################
    # Summoner Database #
    #####################

    _validate_get_summoner_query = Query. \
        has("id").as_(str). \
        or_("accountId").as_(str). \
        or_("puuid").as_(str). \
        or_("name").as_(str).also. \
        has("platform").as_(Platform)

    @get.register(SummonerDto)
    @validate_query(_validate_get_summoner_query, convert_region_to_platform)
    def get_summoner(self, query: MutableMapping[str, Any], context: PipelineContext = None) -> SummonerDto:
        platform_str = query["platform"].value
        if "accountId" in query:
            summoner = self._first(MongoSummoner.objects(platform=platform_str, accountId=query["accountId"]))
        elif "id" in query:
            summoner = self._first(MongoSummoner.objects(platform=platform_str, id=query["id"]))
        elif "puuid" in query:
            summoner = self._first(MongoSummoner.objects(platform=platform_str, puuid=query["puuid"]))
        elif "name" in query:
            summoner = self._first(MongoSummoner.objects(platform=platform_str, name=query["name"]))
        else:
            raise RuntimeError("Impossible!")
        return summoner.to_dto()

    @put.register(SummonerDto)
    def put_summoner(self, item: SummonerDto, context: PipelineContext = None) -> None:

        if "platform" not in item:
            item["platform"] = Region(item["region"]).platform.value
        item["lastUpdate"] = int(datetime.datetime.now().timestamp())
        summoner = MongoSummoner.objects(platform=item["platform"], id=item["id"])
        summoner.update(**item, upsert=True)

    ##################
    # Match Endpoint #
    ##################

    # Match

    _validate_get_match_query = Query. \
        has("id").as_(int).also. \
        has("platform").as_(Platform)

    @get.register(MatchDto)
    @validate_query(_validate_get_match_query, convert_region_to_platform)
    def get_match(self, query: MutableMapping[str, Any], context: PipelineContext = None) -> MatchDto:
        platform_str = query["platform"].value
        match = MongoMatch.objects(platform=platform_str, id=query["id"])
        return match.to_dto()

    @put.register(MatchDto)
    def put_match(self, item: MatchDto, context: PipelineContext = None) -> None:
        print("NO")
        print(item["id"], item["gameId"], item)
