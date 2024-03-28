from uuid import UUID

from pydantic import confloat, constr

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "AddLoanApplicationResponseDTO"
]


class AddLoanApplicationResponseDTO(BaseDomainParserMixin):
    id: UUID
    reference: constr(min_length=16, max_length=16)
    loan_amount: confloat(ge=0)
    loan_granted: bool
    equated_monthly_installment: confloat(ge=0)
    loan_outstanding_balance: confloat(ge=0)
    interest_paid: confloat(ge=0)
    principal_paid: confloat(ge=0)
    amount_paid: confloat(ge=0)
