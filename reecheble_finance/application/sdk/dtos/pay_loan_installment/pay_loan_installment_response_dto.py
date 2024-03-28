from uuid import UUID

from pydantic import confloat, constr

from reecheble_finance.domain.abstract_domain import BaseDomainParserMixin

__all__ = [
    "PayLoanInstallmentResponseDTO"
]


class PayLoanInstallmentResponseDTO(BaseDomainParserMixin):
    id: UUID
    reference: constr(min_length=16, max_length=16)
    outstanding_balance: confloat(ge=0)
    interest_paid: confloat(ge=0)
    principal_paid: confloat(ge=0)
    amount_paid: confloat(ge=0)
