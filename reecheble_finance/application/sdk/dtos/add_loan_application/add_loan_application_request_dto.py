from uuid import UUID

from pydantic import PositiveInt, PositiveFloat, confloat

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "AddLoanApplicationRequestDTO"
]


class AddLoanApplicationRequestDTO(BaseDomainParserMixin):
    account_id: UUID
    request_amount: PositiveFloat = 0
    interest_rate: confloat(ge=0, le=1) = 0.10
    payment_period_in_months: PositiveInt = 18
