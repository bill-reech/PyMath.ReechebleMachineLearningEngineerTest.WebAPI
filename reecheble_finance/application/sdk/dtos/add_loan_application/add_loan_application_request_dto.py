from pydantic import PositiveInt, confloat

from reecheble_finance.application.sdk.dtos.loan_account_dto import LoanAccountDTO
from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "AddLoanApplicationRequestDTO"
]


class AddLoanApplicationRequestDTO(BaseDomainParserMixin):
    account: LoanAccountDTO
    request_amount: PositiveInt = 0
    interest_rate: float
    payment_period_in_months: PositiveInt
    equated_monthly_instalment: confloat(ge=0.00) = 0.00
    principal_paid: confloat(ge=0.00) = 0.00
    interest_paid: confloat(ge=0.00) = 0.00
