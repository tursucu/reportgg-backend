from mongoengine import *
from mongoengine import signals
import datetime
from mongoengine import Document
from mongoengine.fields import (StringField, IntField, LongField, ReferenceField)
from ..common import MongoBaseObject
from kogmaw.dto.match import MatchDto
from kogmaw.dto.common import DtoObject


class MatchParticipantsIdentitiesDto(DtoObject):
    pass


class MatchParticipantsIdentities(Document, MongoBaseObject):
    _dto_type = MatchParticipantsIdentitiesDto
    _table = ["currentPlatformId", "platformId", "match_gameId", "participantId", "accountId", "summonerName",
              "summonerId", "currentAccountId", "profileIcon"]
    p_profileIcon = StringField()
    p_accountId = StringField()
    p_currentAccountId = StringField()
    p_currentPlatformId = StringField()
    p_summonerName = StringField()
    p_summonerId = StringField()
    p_platformId = StringField()
    match_gameId = LongField()
    participantId = IntField()

    def __init__(self, **kwargs):
        player = kwargs.pop("player")
        for key, value in player.items():
            kwargs["p_" + key] = value
        super().__init__(**kwargs)

    def to_dto(self):
        dto = super().to_dto()
        player = {}
        for key, value in list(dto.items()):
            if key.startswith("p_"):
                newkey = key[2:]
                player[newkey] = dto.pop(key)
        dto["player"] = player
        # Create match history Uri
        dto["player"]["matchHistoryUri"] = "/v1/stats/player_history/" + player["platformId"] + "/" + str(player["accountId"])
        return dto


class MatchBanDto(DtoObject):
    pass


class MatchBan(Document, MongoBaseObject):
    _dto_type = MatchBanDto
    _table = ["match_platformId", "match_gameId", "pickTurn", "championId", "teamId"]
    meta = {"collection": "MatchBanDto", "strict": False}
    match_platformId = StringField()
    match_gameId = LongField()
    pickTurn = IntField()
    championId = IntField()
    teamId = IntField()


class MatchTeamDto(DtoObject):
    pass


class MatchTeam(Document, MongoBaseObject):
    _dto_type = MatchTeamDto
    _table = ["match_platformId", "match_gameId", "teamId", "firstDragon", "firstInhibitor", "firstRiftHerald",
              "firstBaron", "firstTower", "firstBlood", "baronKills", "riftHeraldKills", "vilemawKills",
              "inhibitorKills", "towerKills", "dragonKills", "win"]
    meta = {"collection": "MatchTeamDto", "strict": False}
    match_platformId = StringField()
    match_gameId = LongField()
    teamId = IntField()
    firstDragon = BooleanField()
    firstInhibitor = BooleanField()
    firstRiftHerald = BooleanField()
    firstBaron = BooleanField()
    baronKills = IntField()
    riftHeraldKills = IntField()
    vilemawKills = IntField()
    towerKills = IntField()
    dragonKills = IntField()
    win = BooleanField()
    bans = ReferenceField(MatchBan)

    def __init__(self, **dwargs):
        dwargs["win"] = dwargs["win"] == "Win"
        super().__init__(**dwargs)

    def to_dto(self):
        dto = super().to_dto()
        if dto["win"]:
            dto["win"] = "Win"
        else:
            dto["win"] = "Fail"
        return dto


class Match(Document, MongoBaseObject):
    _dto_type = MatchDto
    _table = ["platformId", "gameId", "seasonId", "queueId", "gameVersion", "mapId", "gameDuration",
              "gameCreation", "lastUpdate"]
    meta = {"collection": "MatchDto", "strict": False}
    gameId = LongField()
    queueId = IntField()
    gameType = StringField()
    gameDuration = LongField()
    platformId = StringField()
    gameCreation = LongField()
    seasonId = IntField()
    gameVersion = StringField()
    mapId = IntField()
    gameMode = StringField()
    teams = ReferenceField(MatchTeam)
    participants = ReferenceField(MatchParticipant)
    participantIdentities = ReferenceField(MatchParticipantsIdentities)
