from pydantic import PositiveInt, PositiveFloat, confloat, constr

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "AddLoanApplicationRequestDTO"
]


class AddLoanApplicationRequestDTO(BaseDomainParserMixin):
    account_number: constr(min_length=12, max_length=12)
    request_amount: PositiveFloat = 0
    interest_rate: confloat(ge=0, le=100) = 10
    payment_period_in_months: PositiveInt = 18
