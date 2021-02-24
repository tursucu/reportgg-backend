from mongoengine import *
from mongoengine import signals
import datetime
from mongoengine import Document
from mongoengine.fields import (StringField, IntField, LongField, ReferenceField, DecimalField)
from ..common import MongoBaseObject
from kogmaw.dto.match import MatchDto
from kogmaw.dto.common import DtoObject

class MatchParticipantTimelineDeltasDto(DtoObject):
    pass


class MatchParticipantTimelineDeltas(Document, MongoBaseObject):
    _dto_type = MatchParticipantTimelineDeltasDto
    _table = ["typeId","0-10","10-20","20-30","30-end"]
    meta = {"collection": "match_participant_timeline_deltas", "strict": False}
    typeId = IntField(primary_key=True)
    t_0_10 = DecimalField(precision=7)
    t_10_20 = DecimalField(precision=7)
    t_20_30 = DecimalField(precision=7)
    t_30_end = DecimalField(precision=7)

    def to_dto(self):
        dto = super().to_dto()

        for key, value in list(dto.items()):
            if key.startswith("t_"):
                newkey = key[2:]
                dto[newkey] = dto.pop(key)









class MatchParticipantTimelineDto(DtoObject):
    pass


class MatchParticipantTimeline(Document, MongoBaseObject):
    _dto_type = MatchParticipantTimelineDto
    _table = ["lane", "role"]
    meta = {"collection": "ParticipantTimelineDto", "strict": False}
    role = StringField()
    lane = StringField()
    deltas = ReferenceField(MatchParticipantTimelineDeltas)

    def __init__(self, **kwargs):
        kwargs["deltas"] = [{"type": key, **value}
                            for key, value in kwargs.items()
                            if key.endswith("Deltas")]
        super().__init__(**kwargs)

    def to_dto(self):
        dto = super().to_dto()
        deltas = dto.pop("deltas")
        for delta in deltas:
            dto[delta["type"]] = {key: value for key, value in delta.items() if key != "type"}
        return dto


class MatchParticipantStatsDto(DtoObject):
    pass


class MatchParticipantStats(Document, MongoBaseObject):
    _dto_type = MatchParticipantStatsDto
    _table = ["physicalDamageDealt", "magicDamageDealt", "neutralMinionsKilledTeamJungle", "totalPlayerScore", "deaths",
              "win", "neutralMinionsKilledEnemyJungle", "altarsCaptured", "largestCriticalStrike", "totalDamageDealt",
              "magicDamageDealtToChampions", "visionWardsBoughtInGame", "damageDealtToObjectives",
              "largestKillingSpree", "item1", "quadraKills", "teamObjective", "totalTimeCrowdControlDealt",
              "longestTimeSpentLiving", "wardsKilled", "firstTowerAssist", "firstTowerKill", "item2", "item3", "item0",
              "firstBloodAssist", "visionScore", "wardsPlaced", "item4", "item5", "item6", "turretKills", "tripleKills",
              "damageSelfMitigated", "champLevel", "nodeNeutralizeAssist", "firstInhibitorKill", "goldEarned",
              "magicalDamageTaken", "kills", "doubleKills", "nodeCaptureAssist", "trueDamageTaken", "nodeNeutralize",
              "firstInhibitorAssist", "assists", "unrealKills", "neutralMinionsKilled", "objectivePlayerScore",
              "combatPlayerScore", "damageDealtToTurrets", "altarsNeutralized", "goldSpent", "trueDamageDealt",
              "trueDamageDealtToChampions", "pentaKills", "totalHeal", "totalMinionsKilled", "firstBloodKill",
              "nodeCapture", "largestMultKill", "sightWardsBoughtInGame", "totalDamageDealtToChampions",
              "totalUnitsHealed", "inhibitorKills", "totalScoreRank", "totalDamageTaken", "killingSprees",
              "timeCCingOthers", "physicalDamageTaken", "perk0", "perk0Var1", "perk0Var2", "perk0Var3", "perk1",
              "perk1Var1", "perk1Var2", "perk1Var3", "perk2", "perk2Var1", "perk2Var2", "perk2Var3", "perk3",
              "perk3Var1", "perk3Var2", "perk3Var3", "perk4", "perk4Var1", "perk4Var2", "perk4Var3", "perk5",
              "perk5Var1", "perk5Var2", "perk5Var3", "perkPrimaryStyle", "perkSubStyle"]
    meta = {"collection": "ParticipantStatsDto", "strict": False}
    match_platformId = StringField()
    match_gameId = LongField()
    match_participant_participantId = IntField()
    physicalDamageDealt = IntField()
    magicDamageDealt = IntField()
    neutralMinionsKilledTeamJungle = IntField()
    totalPlayerScore = IntField()
    deaths = IntField()
    win = BooleanField()
    neutralMinionsKilledEnemyJungle = IntField()
    altarsCaptured = IntField()
    largestCriticalStrike = IntField()
    totalDamageDealt = IntField()
    magicDamageDealtToChampions = IntField()
    visionWardsBoughtInGame = IntField()
    damageDealtToObjectives = IntField()
    largestKillingSpree = IntField()
    item1 = IntField()
    quadraKills = IntField()
    teamObjective = IntField()
    totalTimeCrowdControlDealt = IntField()
    longestTimeSpentLiving = IntField()
    wardsKilled = IntField()
    firstTowerAssist = BooleanField()
    firstTowerKill = BooleanField()
    item2 = IntField()
    item3 = IntField()
    item0 = IntField()
    firstBloodAssist = BooleanField()
    visionScore = IntField()
    wardsPlaced = IntField()
    item4 = IntField()
    item5 = IntField()
    item6 = IntField()
    turretKills = IntField()
    tripleKills = IntField()
    damageSelfMitigated = IntField()
    champLevel = IntField()
    nodeNeutralizeAssist = IntField()
    firstInhibitorKill = BooleanField()
    goldEarned = IntField()
    magicalDamageTaken = IntField()
    kills = IntField()
    doubleKills = IntField()
    nodeCaptureAssist = IntField()
    trueDamageTaken = IntField()
    nodeNeutralize = IntField()
    firstInhibitorAssist = BooleanField()
    assists = IntField()
    unrealKills = IntField()
    neutralMinionsKilled = IntField()
    objectivePlayerScore = IntField()
    combatPlayerScore = IntField()
    damageDealtToTurrets = IntField()
    altarsNeutralized = IntField()
    goldSpent = IntField()
    trueDamageDealt = IntField()
    trueDamageDealtToChampions = IntField()
    pentaKills = IntField()
    totalHeal = IntField()
    totalMinionsKilled = IntField()
    firstBloodKill = BooleanField()
    nodeCapture = IntField()
    largestMultKill = IntField()
    sightWardsBoughtInGame = IntField()
    totalDamageDealtToChampions = IntField()
    totalUnitsHealed = IntField()
    inhibitorKills = IntField()
    totalScoreRank = IntField()
    totalDamageTaken = IntField()
    killingSprees = IntField()
    timeCCingOthers = IntField()
    physicalDamageTaken = IntField()
    perk0 = IntField()
    perk0Var1 = IntField()
    perk0Var2 = IntField()
    perk0Var3 = IntField()
    perk1 = IntField()
    perk1Var1 = IntField()
    perk1Var2 = IntField()
    perk1Var3 = IntField()
    perk2 = IntField()
    perk2Var1 = IntField()
    perk2Var2 = IntField()
    perk2Var3 = IntField()
    perk3 = IntField()
    perk3Var1 = IntField()
    perk3Var2 = IntField()
    perk3Var3 = IntField()
    perk4 = IntField()
    perk4Var1 = IntField()
    perk4Var2 = IntField()
    perk4Var3 = IntField()
    perk5 = IntField()
    perk5Var1 = IntField()
    perk5Var2 = IntField()
    perk5Var3 = IntField()
    perkPrimaryStyle = IntField()
    perkSubStyle = IntField()


class MatchParticipantDto(DtoObject):
    pass


class MatchParticipant(Document, MongoBaseObject):
    _dto_type = MatchParticipantDto
    _table = ["participantId", "championId", "teamId", "spell1Id", "spell2Id"]
    meta = {"collection": "ParticipantDto", "strict": False}
    match_platformId = StringField()
    match_gameId = LongField()
    participantId = IntField()
    championId = IntField()
    teamId = IntField()
    spell1Id = IntField()
    spell2Id = IntField()
    stats = ReferenceField(MatchParticipantStats)
    timeline = ReferenceField(MatchParticipantTimeline)


class MatchParticipantsIdentitiesDto(DtoObject):
    pass


class MatchParticipantsIdentities(Document, MongoBaseObject):
    _dto_type = MatchParticipantsIdentitiesDto
    _table = ["currentPlatformId", "platformId", "match_gameId", "participantId", "accountId", "summonerName",
              "summonerId", "currentAccountId", "profileIcon"]
    meta = {"collection": "ParticipantIdentityDto", "strict": False}
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
        dto["player"]["matchHistoryUri"] = "/v1/stats/player_history/" + player["platformId"] + "/" + str(
            player["accountId"])
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
