from mongoengine import *
from mongoengine import Document
from mongoengine.fields import (StringField, IntField, LongField, DecimalField, EmbeddedDocumentListField,
                                EmbeddedDocument, EmbeddedDocumentField)
from ..common import MongoBaseObject
from kogmaw.dto.match import MatchDto
from kogmaw.dto.common import DtoObject


class MatchParticipantTimelineDeltasDto(DtoObject):
    pass


class MatchParticipantTimelineDeltas(EmbeddedDocument, MongoBaseObject):
    _table = ["t_0_10", "t_10_20", "t_20_30", "t_30_end"]
    t_0_10 = FloatField(precision=7)
    t_10_20 = FloatField(precision=7)
    t_20_30 = FloatField(precision=7)
    t_30_end = FloatField(precision=7)

    def __init__(self, **kwargs):
        if '0-10' in kwargs:
            kwargs['t_0_10'] = kwargs.pop("0-10")
        if '10-20' in kwargs:
            kwargs['t_10_20'] = kwargs.pop("10-20")
        if '20-30' in kwargs:
            kwargs['t_20_30'] = kwargs.pop("20-30")
        if '30-end' in kwargs:
            kwargs['t_30_end'] = kwargs.pop("30-end")
        super().__init__(**kwargs)

    def to_dto(self):
        map = {}
        for column in self._table:
            if column == 't_0_10':
                key = '0-10'
            if column == 't_10_20':
                key = '10-20'
            if column == 't_20_30':
                key = '20-30'
            if column == 't_30_end':
                key = '30-end'
            if getattr(self, column) is not None:
                map[key] = getattr(self, column)
        return map


class MatchParticipantTimelineDto(DtoObject):
    pass


class MatchParticipantTimeline(EmbeddedDocument, MongoBaseObject):
    _dto_type = MatchParticipantTimelineDto
    _table = ["participantId", "role", "lane"]
    participantId = IntField()
    role = StringField()
    lane = StringField()
    damageTakenDiffPerMinDeltas = EmbeddedDocumentField(MatchParticipantTimelineDeltas)
    goldPerMinDeltas = EmbeddedDocumentField(MatchParticipantTimelineDeltas)
    xpPerMinDeltas = EmbeddedDocumentField(MatchParticipantTimelineDeltas)
    creepsPerMinDeltas = EmbeddedDocumentField(MatchParticipantTimelineDeltas)
    damageTakenPerMinDeltas = EmbeddedDocumentField(MatchParticipantTimelineDeltas)
    goldPerMinDeltas = EmbeddedDocumentField(MatchParticipantTimelineDeltas)
    xpPerMinDeltas = EmbeddedDocumentField(MatchParticipantTimelineDeltas)
    creepsPerMinDeltas = EmbeddedDocumentField(MatchParticipantTimelineDeltas)
    csDiffPerMinDeltas = EmbeddedDocumentField(MatchParticipantTimelineDeltas)
    damageTakenDiffPerMinDeltas = EmbeddedDocumentField(MatchParticipantTimelineDeltas)
    xpDiffPerMinDeltas = EmbeddedDocumentField(MatchParticipantTimelineDeltas)
    _relationships = ["damageTakenDiffPerMinDeltas", "goldPerMinDeltas", "xpPerMinDeltas", "creepsPerMinDeltas",
                      "damageTakenPerMinDeltas", "goldPerMinDeltas", "xpPerMinDeltas", "creepsPerMinDeltas",
                      "csDiffPerMinDeltas", "damageTakenDiffPerMinDeltas", "xpDiffPerMinDeltas"]

    def to_dto(self):
        map = {}
        for column in self._table:
            if getattr(self, column) is not None:
                map[column] = getattr(self, column)

        if self.damageTakenDiffPerMinDeltas:
            map["damageTakenDiffPerMinDeltas"] = self.damageTakenDiffPerMinDeltas.to_dto()
        if self.goldPerMinDeltas:
            map["goldPerMinDeltas"] = self.goldPerMinDeltas.to_dto()
        if self.xpPerMinDeltas:
            map["xpPerMinDeltas"] = self.xpPerMinDeltas.to_dto()
        if self.creepsPerMinDeltas:
            map["creepsPerMinDeltas"] = self.creepsPerMinDeltas.to_dto()
        if self.damageTakenPerMinDeltas:
            map["damageTakenPerMinDeltas"] = self.damageTakenPerMinDeltas.to_dto()
        if self.goldPerMinDeltas:
            map["goldPerMinDeltas"] = self.goldPerMinDeltas.to_dto()
        if self.xpPerMinDeltas:
            map["xpPerMinDeltas"] = self.xpPerMinDeltas.to_dto()
        if self.creepsPerMinDeltas:
            map["creepsPerMinDeltas"] = self.creepsPerMinDeltas.to_dto()
        if self.csDiffPerMinDeltas:
            map["csDiffPerMinDeltas"] = self.csDiffPerMinDeltas.to_dto()
        if self.damageTakenDiffPerMinDeltas:
            map["damageTakenDiffPerMinDeltas"] = self.damageTakenDiffPerMinDeltas.to_dto()
        if self.xpDiffPerMinDeltas:
            map["xpDiffPerMinDeltas"] = self.xpDiffPerMinDeltas.to_dto()
        return map


class MatchParticipantStatsDto(DtoObject):
    pass


class MatchParticipantStats(EmbeddedDocument, MongoBaseObject):
    _dto_type = MatchParticipantStatsDto
    _table = ["participantId", "physicalDamageDealt", "magicDamageDealt", "neutralMinionsKilledTeamJungle",
              "totalPlayerScore", "deaths", "win", "neutralMinionsKilledEnemyJungle", "altarsCaptured",
              "largestCriticalStrike", "totalDamageDealt", "magicDamageDealtToChampions", "visionWardsBoughtInGame",
              "damageDealtToObjectives", "largestKillingSpree", "item1", "quadraKills", "teamObjective",
              "totalTimeCrowdControlDealt", "longestTimeSpentLiving", "wardsKilled", "firstTowerAssist",
              "firstTowerKill", "item2", "item3", "item0", "firstBloodAssist", "visionScore", "wardsPlaced", "item4",
              "item5", "item6", "turretKills", "tripleKills", "damageSelfMitigated", "champLevel",
              "nodeNeutralizeAssist", "firstInhibitorKill", "goldEarned", "magicalDamageTaken", "kills", "doubleKills",
              "nodeCaptureAssist", "trueDamageTaken", "nodeNeutralize", "firstInhibitorAssist", "assists",
              "unrealKills", "neutralMinionsKilled", "objectivePlayerScore", "combatPlayerScore",
              "damageDealtToTurrets", "altarsNeutralized", "goldSpent", "trueDamageDealt", "trueDamageDealtToChampions",
              "pentaKills", "totalHeal", "totalMinionsKilled", "firstBloodKill", "nodeCapture", "largestMultKill",
              "sightWardsBoughtInGame", "totalDamageDealtToChampions", "totalUnitsHealed", "inhibitorKills",
              "totalScoreRank", "totalDamageTaken", "killingSprees", "timeCCingOthers", "physicalDamageTaken", "perk0",
              "perk0Var1", "perk0Var2", "perk0Var3", "perk1", "perk1Var1", "perk1Var2", "perk1Var3", "perk2",
              "perk2Var1", "perk2Var2", "perk2Var3", "perk3", "perk3Var1", "perk3Var2", "perk3Var3", "perk4",
              "perk4Var1", "perk4Var2", "perk4Var3", "perk5", "perk5Var1", "perk5Var2", "perk5Var3", "perkPrimaryStyle",
              "perkSubStyle", "playerScore3", "statPerk1", "playerScore8", "playerScore2", "playerScore4",
              "playerScore7", "largestMultiKill", "playerScore5", "playerScore9", "physicalDamageDealtToChampions",
              "playerScore0", "statPerk0", "statPerk2", "playerScore1", "playerScore6"]
    participantId = IntField()
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
    playerScore3 = IntField()
    statPerk1 = IntField()
    playerScore8 = IntField()
    playerScore2 = IntField()
    playerScore4 = IntField()
    playerScore7 = IntField()
    largestMultiKill = IntField()
    playerScore5 = IntField()
    playerScore9 = IntField()
    physicalDamageDealtToChampions = IntField()
    playerScore0 = IntField()
    statPerk0 = IntField()
    statPerk2 = IntField()
    playerScore1 = IntField()
    playerScore6 = IntField()

    def to_dto(self):
        map = {}
        for column in self._table:
            if getattr(self, column) is not None:
                map[column] = getattr(self, column)
        return map


class MatchParticipantDto(DtoObject):
    pass


class MatchParticipant(EmbeddedDocument, MongoBaseObject):
    _dto_type = MatchParticipantDto
    _table = ["participantId", "championId", "teamId", "spell1Id", "spell2Id"]
    participantId = IntField()
    championId = IntField()
    teamId = IntField()
    spell1Id = IntField()
    spell2Id = IntField()
    stats = EmbeddedDocumentField("MatchParticipantStats")
    timeline = EmbeddedDocumentField("MatchParticipantTimeline")
    _relationships = ["stats", "timeline"]

    def to_dto(self):
        map = {}
        for column in self._table:
            if getattr(self, column) is not None:
                map[column] = getattr(self, column)
        if hasattr(self, "stats"):
            map["stats"] = self.stats.to_dto()
        if hasattr(self, "timeline"):
            map["timeline"] = self.timeline.to_dto()
        return map


class MatchPlayerDto(DtoObject):
    pass


class MatchPlayer(EmbeddedDocument, MongoBaseObject):
    _dto_type = MatchPlayerDto
    _table = ["platformId", "accountId", "summonerName", "summonerId", "currentPlatformId", "currentAccountId",
              "matchHistoryUri", "profileIcon"]
    platformId = StringField()
    accountId = StringField()
    summonerName = StringField()
    summonerId = StringField()
    currentPlatformId = StringField()
    currentAccountId = StringField()
    matchHistoryUri = StringField()
    profileIcon = IntField()

    def to_dto(self):
        map = {}
        for column in self._table:
            if getattr(self, column) is not None:
                map[column] = getattr(self, column)
        return map


class MatchParticipantsIdentitiesDto(DtoObject):
    pass


class MatchParticipantsIdentities(EmbeddedDocument, MongoBaseObject):
    _dto_type = MatchParticipantsIdentitiesDto
    _table = ["participantId"]
    participantId = IntField()
    player = EmbeddedDocumentField("MatchPlayer")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_dto(self):
        map = {}
        for column in self._table:
            if getattr(self, column) is not None:
                map[column] = getattr(self, column)

        if hasattr(self, "player"):
            map["player"] = self.player.to_dto()
        return map


class MatchBanDto(DtoObject):
    pass


class MatchBan(EmbeddedDocument, MongoBaseObject):
    _dto_type = MatchBanDto
    _table = ["pickTurn", "championId"]
    pickTurn = IntField()
    championId = IntField()

    def to_dto(self):
        map = {}
        for column in self._table:
            if getattr(self, column) is not None:
                map[column] = getattr(self, column)
        return map


class MatchTeamDto(DtoObject):
    pass


class MatchTeam(EmbeddedDocument, MongoBaseObject):
    _table = ["teamId", "firstDragon", "firstInhibitor", "firstRiftHerald", "firstBaron", "firstTower", "firstBlood",
              "baronKills", "riftHeraldKills", "vilemawKills", "inhibitorKills", "towerKills", "dragonKills",
              "dominionVictoryScore", "win"]
    teamId = IntField()
    firstDragon = BooleanField()
    firstInhibitor = BooleanField()
    firstRiftHerald = BooleanField()
    firstBaron = BooleanField()
    firstTower = BooleanField()
    firstBlood = BooleanField()
    baronKills = IntField()
    riftHeraldKills = IntField()
    vilemawKills = IntField()
    inhibitorKills = IntField()
    towerKills = IntField()
    dragonKills = IntField()
    dominionVictoryScore = IntField()
    win = BooleanField()
    bans = EmbeddedDocumentListField("MatchBan")

    def to_dto(self):
        map = {}
        for column in self._table:
            if getattr(self, column) is not None:
                map[column] = getattr(self, column)

        if hasattr(self, "bans"):
            if isinstance(self.bans, list):
                map["bans"] = [v.to_dto() for v in self.bans]
        return map


class Key(EmbeddedDocument):
    gameId = LongField()
    platformId = StringField()


class Match(Document, MongoBaseObject):
    _dto_type = MatchDto
    _table = ["platformId", "gameId", "seasonId", "queueId", "gameVersion", "mapId", "gameDuration",
              "gameCreation", "lastUpdate", "region"]
    meta = {"collection": "MatchDto", "strict": False}
    key = EmbeddedDocumentField("Key", primary_key=True)
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
    lastUpdate = LongField()
    teams = ListField(EmbeddedDocumentField("MatchTeam"))
    participants = ListField(EmbeddedDocumentField("MatchParticipant"))
    participantIdentities = ListField(EmbeddedDocumentField("MatchParticipantsIdentities"))
    region = StringField()
