from datetime import date
from typing import List
from uuid import UUID

from pydantic import confloat, PositiveInt, constr

from reecheble_finance.application.sdk.dtos.get_loan_history_snapshot.get_loan_installment_history_snapshot_response import (
    GetLoanInstallmentHistorySnapshotResponseDTO)
from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "GetAccountLoanResponseDTO"
]


class GetAccountLoanResponseDTO(BaseDomainParserMixin):
    id: UUID
    reference: constr(min_length=16, max_length=16)
    request_amount: confloat(ge=0)
    interest_rate: confloat(ge=0, le=100)
    payment_period_in_months: PositiveInt
    origination_date: date
    due_date: date
    equated_monthly_installment: confloat(ge=0.00)
    latest_principal_paid: confloat(ge=0.00)
    latest_interest_paid: confloat(ge=0.00)
    repayment_history: List[GetLoanInstallmentHistorySnapshotResponseDTO] = []
