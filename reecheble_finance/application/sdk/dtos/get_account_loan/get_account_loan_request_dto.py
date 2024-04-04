from pydantic import constr

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "GetAccountLoanRequestDTO"
]


class GetAccountLoanRequestDTO(BaseDomainParserMixin):
    account_number: constr(min_length=12, max_length=12)
