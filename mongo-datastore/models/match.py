from mongoengine import *
from mongoengine import signals
import datetime
from mongoengine import Document
from mongoengine.fields import (StringField, IntField, LongField)
from ..common import MongoBaseObject
from kogmaw.dto.match import MatchDto

class Match(Document, MongoBaseObject):
    _dto_type = MatchDto
    _table = ["platformId", "gameId", "seasonId", "queueId", "gameVersion", "mapId", "gameDuration",
              "gameCreation","lastUpdate"]
    meta = {"collection": "MatchDto", "strict": False}
    platformId = StringField()
    gameId = LongField()
    seasonId = IntField()
    queueId = IntField()
    gameVersion = StringField()
    mapId = IntField()
    gameDuration = LongField()
    gameCreation = LongField()
    lastUpdate = LongField()
