from abc import ABC

from reecheble_finance.domain.abstract_domain import BaseDomainParserMixin

__all__ = [
    "AbstractQuery",
    "BaseQuery"
]


class AbstractQuery(ABC):
    ...


class BaseQuery(BaseDomainParserMixin, AbstractQuery):
    ...
