"""
A loan installment history query handler module.
"""

import sys
from typing import List

from reecheble_finance.application.sdk.dtos.get_loan_history_snapshot.get_loan_installment_history_snapshot_response import (
    GetLoanInstallmentHistorySnapshotResponseDTO)
from reecheble_finance.application.services.abstract_service import AbstractApplicationService
from reecheble_finance.application.services.loan_service.get_loan_installment_history.get_loan_installment_history_query import (
    GetLoanInstallmentHistoryQuery)
from reecheble_finance.domain.abstract_repository import RepositoryContextSession
from reecheble_finance.domain.enums.response_status.response_status import ResponseStatusEnum
from reecheble_finance.domain.models.loan_request import LoanRequest
from reecheble_finance.infrastructure.data_access.repositories.loan_repository.abstract_loan_repository import \
    AbstractLoanRepository
from reecheble_finance.infrastructure.data_access.repositories.loan_repository.loan_repository import LoanRepository
from reecheble_finance.shared.result.result import Result, FailureResult, SuccessResult


class GetLoanInstallmentHistoryQueryHandler(AbstractApplicationService):

    def __init__(self, context: RepositoryContextSession) -> None:
        super().__init__(context=context)
        self.loan_repository: AbstractLoanRepository = LoanRepository(context=self.context)

    async def handle(self, query: GetLoanInstallmentHistoryQuery) -> Result[
        List[GetLoanInstallmentHistorySnapshotResponseDTO]]:
        """
        Asynchronous loan installment history query request handler.

        :param query: Loan installment history query.
        """

        try:
            loan_request: LoanRequest = self.loan_repository.get(id=query.data.id)
            return SuccessResult(
                data=[GetLoanInstallmentHistorySnapshotResponseDTO(**req.dict()) for req in
                      loan_request.repayment_history],
                status=ResponseStatusEnum.success)

        except Exception as ex:
            print(f"Error: {ex}", file=sys.stderr)
            return FailureResult(data=None, status=ResponseStatusEnum.fail, message="That was definitely not expected")
