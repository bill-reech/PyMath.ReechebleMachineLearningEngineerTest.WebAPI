"""
A Reecheble Finance loan installment history query module.
"""

from reecheble_finance.application.sdk.dtos.get_loan_history_snapshot.get_loan_installment_history_snapshot_request import (
    GetLoanInstallmentHistorySnapshotRequestDTO)
from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "GetLoanInstallmentHistoryQuery"
]


class GetLoanInstallmentHistoryQuery(BaseDomainParserMixin):
    """
     Reecheble Finance loan installment query.

     :param data: Reecheble Finance loan installment history query details
     """
    data: GetLoanInstallmentHistorySnapshotRequestDTO
