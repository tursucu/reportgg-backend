from mongoengine import *
from mongoengine import signals
import datetime
from mongoengine import Document
from mongoengine.fields import (StringField, IntField, LongField)
from ..common import MongoBaseObject
from kogmaw.dto.summoner import SummonerDto

def handler(event):
    """Signal decorator to allow use of callback functions as class decorators."""

    def decorator(fn):
        def apply(cls):
            event.connect(fn, sender=cls)
            return cls

        fn.apply = apply
        return fn

    return decorator


@handler(signals.pre_save)
def update_modified(sender, document):
    print("PRE")

@update_modified.apply
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
