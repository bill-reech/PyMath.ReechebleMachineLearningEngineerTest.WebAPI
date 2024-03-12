"""
Abstract repositories.
"""

from typing import TypeVar
from abc import ABC, abstractmethod

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import AbstractDomainParser

__all__ = [
    "ApplicationModel",
    "RepositoryContextSession",
    "AbstractRepository",
    "SqlAlchemyRelationalAbstractRepository"
]


ApplicationModel = TypeVar("ApplicationModel", bound=AbstractDomainParser)
RepositoryContextSession = TypeVar("RepositoryContextSession")


class AbstractRepository(ABC):
    """
    Abstract repository.
    """

    def __init__(self, context: RepositoryContextSession) -> None:
        self.context = context

    @abstractmethod
    def sync(self) -> None: ...

    @abstractmethod
    def add(self, *args, **kwargs) -> ApplicationModel: ...

    @abstractmethod
    def list(self, *args, **kwargs) -> ApplicationModel: ...

    @abstractmethod
    def get(self, **filters): ...

    @abstractmethod
    def update(self, **kwargs): ...

    @abstractmethod
    def delete(self, id_): ...


class SqlAlchemyRelationalAbstractRepository(AbstractRepository, ABC):
    """
    Abstract repository using the SqlAlchemy as the `Object Relational Mapper`.
    """

    def __init__(self, context: RepositoryContextSession) -> None:
        self.relational_context: RepositoryContextSession = context
        super().__init__(context=self.relational_context)

    def sync(self) -> None:
        self.context.flush()
