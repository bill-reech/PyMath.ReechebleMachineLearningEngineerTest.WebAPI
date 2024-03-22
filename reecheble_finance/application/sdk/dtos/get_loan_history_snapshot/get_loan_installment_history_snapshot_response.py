from uuid import UUID

from pydantic import conint, confloat

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "GetLoanInstallmentHistorySnapshotResponseDTO"
]


class GetLoanInstallmentHistorySnapshotResponseDTO(BaseDomainParserMixin):
    id: UUID
    month: conint(ge=0)
    equated_monthly_instalment: confloat(ge=0)
    principal_paid: confloat(ge=0.00)
    interest_paid: confloat(ge=0.00)
    loan_balance: confloat(ge=0.00)
