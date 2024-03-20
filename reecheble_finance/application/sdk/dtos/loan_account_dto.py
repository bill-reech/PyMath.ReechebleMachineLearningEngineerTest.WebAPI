from pydantic import PositiveFloat

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "LoanAccountDTO"
]


class LoanAccountDTO(BaseDomainParserMixin):
    ...
