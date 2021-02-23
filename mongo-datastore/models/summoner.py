from mongoengine import *
from mongoengine import signals
import datetime
from mongoengine import Document
from mongoengine.fields import (StringField, IntField, LongField)
from ..common import MongoBaseObject
from kogmaw.dto.summoner import SummonerDto

class Summoner(Document, MongoBaseObject):
    _dto_type = SummonerDto
    _table = ["id", "accountId", "puuid", "name", "profileIconId", "revisionDate", "summonerLevel", "lastUpdate",
              "platform"]
    meta = {"collection": "SummonerDto", "strict": False}
    region = StringField()
    id = StringField()
    accountId = StringField()
    puuid = StringField()
    name = StringField()
    profileIconId = IntField()
    revisionDate = LongField()
    summonerLevel = LongField()
    lastUpdate = LongField()
    platform = StringField()
