"""
Abstract loan account repository.
"""

from abc import abstractmethod

from reecheble_finance.domain.abstract_repository.abstract_repository import (
    RepositoryContextSession,
    AbstractRepository
)

__all__ = [
    "AbstractLoanAccountRepository"
]


class AbstractLoanAccountRepository(AbstractRepository):
    """
    Abstract loan account repository.
    """

    def __init__(self, context: RepositoryContextSession) -> None:
        super().__init__(context=context)

    @abstractmethod
    def add(self, *, request):
        ...

    @abstractmethod
    def list(self):
        ...

    @abstractmethod
    def get(self, **filters):
        ...

    @abstractmethod
    def get_many(self, **filters):
        ...

    @abstractmethod
    def update(self, **kwargs):
        ...

    @abstractmethod
    def delete(self, id_):
        ...
