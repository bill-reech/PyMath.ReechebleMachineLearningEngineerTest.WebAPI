from uuid import UUID

from pydantic import confloat

from reecheble_finance.domain.abstract_domain import BaseDomainParserMixin

__all__ = [
    "PayLoanInstallmentResponseDTO"
]


class PayLoanInstallmentResponseDTO(BaseDomainParserMixin):
    loan_id: UUID
    loan_outstanding_balance: confloat(ge=0)
