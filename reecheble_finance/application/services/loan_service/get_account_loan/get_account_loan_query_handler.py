import sys
from typing import List

from reecheble_finance.application.sdk.dtos.get_account_loan.get_account_loan_response_dto import (
    GetAccountLoanResponseDTO)
from reecheble_finance.application.services.abstract_service import AbstractApplicationService
from reecheble_finance.application.services.loan_service.get_account_loan.get_account_loan_query import (
    GetAccountLoanQuery)
from reecheble_finance.domain.abstract_repository.abstract_repository import RepositoryContextSession
from reecheble_finance.domain.enums.response_status.response_status import ResponseStatusEnum
from reecheble_finance.domain.models.loan_request import LoanRequest
from reecheble_finance.infrastructure.data_access.repositories.loan_repository.abstract_loan_repository import (
    AbstractLoanRepository)
from reecheble_finance.infrastructure.data_access.repositories.loan_repository.loan_repository import LoanRepository
from reecheble_finance.shared.result.result import Result, SuccessResult, FailureResult


class GetAccountLoanQueryHandler(AbstractApplicationService):

    def __init__(self, context: RepositoryContextSession) -> None:
        super().__init__(context=context)
        self.loan_repository: AbstractLoanRepository = LoanRepository(context=self.context)

    async def handle(self, query: GetAccountLoanQuery) -> Result[List[GetAccountLoanResponseDTO]]:
        """
        Asynchronous account loans query request handler.
        """

        try:
            loan_accounts: List[LoanRequest] = self.loan_repository.get_many(account_number=query.data.account_number)
            return SuccessResult(
                data=[GetAccountLoanResponseDTO(**req.dict()) for req in loan_accounts],
                status=ResponseStatusEnum.success)

        except Exception as ex:
            print(f"Error: {ex}", file=sys.stderr)
            return FailureResult(data=None, status=ResponseStatusEnum.fail, message="That was definitely not expected")
