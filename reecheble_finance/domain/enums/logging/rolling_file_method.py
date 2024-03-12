from enum import Enum

__all__ = [
    "RollingFileMethodEnum"
]


class RollingFileMethodEnum(int, Enum):
    by_max_size = 1
    daily = 2
