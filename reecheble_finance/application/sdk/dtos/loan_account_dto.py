from pydantic import PositiveFloat

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin


class LoanAccountDTO(BaseDomainParserMixin):
    outstanding_balance: PositiveFloat = 0.00
