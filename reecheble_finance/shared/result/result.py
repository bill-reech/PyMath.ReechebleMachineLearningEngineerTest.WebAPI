from typing import TypeVar, Generic

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin
from reecheble_finance.domain.enums.response_status.response_status import ResponseStatusEnum

__all__ = ["Result", "SuccessResult"]

DataT = TypeVar("DataT")


class Result(BaseDomainParserMixin, Generic[DataT]):
    data: DataT | None
    message: str | None = None
    status: ResponseStatusEnum


class SuccessResult(Result):
    ...
