from typing import Type

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin
from reecheble_finance.infrastructure.data_access.context import ServiceContext

__all__ = [
    "PathDependency"
]


class PathDependency(BaseDomainParserMixin):
    context: Type[ServiceContext]
