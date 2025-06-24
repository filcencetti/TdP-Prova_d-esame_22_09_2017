from dataclasses import dataclass
from datetime import datetime

@dataclass
class Race:
    raceId : int
    year : int
    round : int
    circuitId : int
    name : str
    date : datetime
    time : datetime
    url : str

    def __hash__(self):
        return hash(self.raceId)
    def __eq__(self, other):
        return self.raceId == other.raceId
    def __str__(self):
        return f"{self.name} ({self.raceId})"