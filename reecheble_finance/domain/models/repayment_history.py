from uuid import UUID

from pydantic import conint, confloat

from reecheble_finance.domain.abstract_domain import BaseDomainParserMixin


class RepaymentHistory(BaseDomainParserMixin):
    id: UUID
    month: conint(ge=0)
    equated_monthly_instalment: confloat(ge=0) = 0.00
    principal_paid: confloat(ge=0.00) = 0.00
    interest_paid: confloat(ge=0.00) = 0.00
    loan_balance: confloat(ge=0.00) = 0.00
