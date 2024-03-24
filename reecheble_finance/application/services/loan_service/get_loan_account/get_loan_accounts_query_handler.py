import sys
from typing import List

from reecheble_finance.application.sdk.dtos.get_loan_account.get_loan_account_response_dto import (
    GetLoanAccountResponseDTO)
from reecheble_finance.application.services.abstract_service import AbstractApplicationService
from reecheble_finance.application.services.loan_service.get_loan_account.get_loan_accounts_query import (
    GetLoanAccountsQuery)
from reecheble_finance.domain.abstract_repository.abstract_repository import RepositoryContextSession
from reecheble_finance.domain.enums.response_status.response_status import ResponseStatusEnum
from reecheble_finance.domain.models.loan_account import LoanAccount
from reecheble_finance.infrastructure.data_access.repositories.loan_account_repository.abstract_loan_account_repository import (
    AbstractLoanAccountRepository)
from reecheble_finance.infrastructure.data_access.repositories.loan_account_repository.loan_account_repository import (
    LoanAccountRepository)
from reecheble_finance.shared.result.result import Result, SuccessResult, FailureResult


class GetLoanAccountsQueryHandler(AbstractApplicationService):

    def __init__(self, context: RepositoryContextSession) -> None:
        super().__init__(context=context)
        self.loan_account_repository: AbstractLoanAccountRepository = LoanAccountRepository(context=self.context)

    async def handle(self, query: GetLoanAccountsQuery) -> Result[List[GetLoanAccountResponseDTO]]:
        """
        Asynchronous loan accounts query request handler.
        """

        try:
            loan_accounts: List[LoanAccount] = self.loan_account_repository.list()
            return SuccessResult(
                data=[GetLoanAccountResponseDTO(**req.dict()) for req in loan_accounts],
                status=ResponseStatusEnum.success)

        except Exception as ex:
            print(f"Error: {ex}", file=sys.stderr)
            return FailureResult(data=None, status=ResponseStatusEnum.fail, message="That was definitely not expected")
