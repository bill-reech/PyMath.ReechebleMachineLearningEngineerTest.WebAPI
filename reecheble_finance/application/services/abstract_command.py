from abc import ABC

from reecheble_finance.domain.abstract_domain import BaseDomainParserMixin

__all__ = [
    "AbstractCommand",
    "BaseCommand"
]


class AbstractCommand(ABC):
    ...


class BaseCommand(BaseDomainParserMixin, AbstractCommand):
    ...
