from abc import ABC

__all__ = [
    "AbstractApplicationService"
]


class AbstractApplicationService(ABC):

    def __init__(self, context) -> None:
        self.context = context
