# OS
from enum import Enum


class StatusType(Enum):
    assigned = (1, "Assigned")
    failed = (2, "Failed")
    completed = (3, "Completed")

    @classmethod
    def get_value(cls, member):
        return cls[member].value[0]

    @classmethod
    def choices(cls):
        return [x.value for x in cls]
