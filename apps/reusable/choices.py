# OS
from enum import IntEnum


class StatusType(IntEnum):
    assigned = 1
    failed = 2
    completed = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def choices_hitman(cls):
        choices = [(key.value, key.name) if key.value != 1 else None for key in cls]
        del choices[0]
        return choices
