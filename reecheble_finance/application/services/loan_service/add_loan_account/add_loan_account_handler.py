"""
A loan account creation command handler module.
"""
import uuid

from reecheble_finance.application.sdk.dtos.add_loan_account.add_loan_account_response_dto import (
    AddLoanAccountResponseDTO)
from reecheble_finance.application.services.abstract_service import AbstractApplicationService
from reecheble_finance.application.services.loan_service.add_loan_account import AddLoanAccountCommand
from reecheble_finance.domain.abstract_repository.abstract_repository import RepositoryContextSession
from reecheble_finance.domain.enums.response_status.response_status import ResponseStatusEnum
from reecheble_finance.domain.models.loan_account import LoanAccount
from reecheble_finance.infrastructure.data_access.repositories.loan_account_repository.abstract_loan_account_repository import (
    AbstractLoanAccountRepository)
from reecheble_finance.infrastructure.data_access.repositories.loan_account_repository.loan_account_repository import (
    LoanAccountRepository)
from reecheble_finance.shared.result.result import SuccessResult, Result


class AddLoanAccountCommandHandler(AbstractApplicationService):

    def __init__(self, context: RepositoryContextSession) -> None:
        super().__init__(context=context)
        self.repository: AbstractLoanAccountRepository = LoanAccountRepository(context=self.context)

    async def handle(self, command: AddLoanAccountCommand) -> Result[AddLoanAccountResponseDTO]:
        """
        Asynchronous loan account creation request handler.

        :param command: Loan account creation command
        """

        loan_account = LoanAccount(
            id=uuid.uuid4(),
            outstanding_balance=0.00,
            first_name=command.data.first_name,
            last_name=command.data.last_name,
            email_address=command.data.email_address
        )
        loan_account = self.repository.add(request=loan_account)
        return SuccessResult(data=AddLoanAccountResponseDTO(**loan_account.dict()), status=ResponseStatusEnum.succeed)
