from abc import ABC

from reecheble_finance.domain.abstract_repository.abstract_repository import RepositoryContextSession

__all__ = [
    "AbstractApplicationService"
]


class AbstractApplicationService(ABC):

    def __init__(self, context: RepositoryContextSession) -> None:
        self.context = context
