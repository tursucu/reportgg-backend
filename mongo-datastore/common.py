import datetime, threading, time
from typing import Mapping
from abc import abstractmethod
import json


class MongoBaseObject(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dto(self):
        map = {}
        for column in self._table:
            if getattr(self, column) is not None:
                map[column] = getattr(self, column)
        if hasattr(self, "teams"):
            if isinstance(self.teams, list):
                map["teams"] = [v.to_dto() for v in self.teams]
        if hasattr(self, "participants"):
            if isinstance(self.participants, list):
                map["participants"] = [v.to_dto() for v in self.participants]
        if hasattr(self, "participantIdentities"):
            if isinstance(self.participantIdentities, list):
                map["participantIdentities"] = [v.to_dto() for v in self.participantIdentities]
        return self._dto_type(map)

    def has_expired(self, expirations: Mapping[type, float]) -> bool:
        if hasattr(self, "lastUpdate"):
            expire_seconds = expirations.get(self._dto_type, -1)
            if expire_seconds > 0:
                now = datetime.datetime.now().timestamp()
                return now > (self.lastUpdate if self.lastUpdate else 0) + expire_seconds
        return False

    def updated(self):
        if hasattr(self, "lastUpdate"):
            self.lastUpdate = datetime.datetime.now().timestamp()

    @abstractmethod
    def _table(self):
        pass

    @abstractmethod
    def _dto_type(self):
        pass
