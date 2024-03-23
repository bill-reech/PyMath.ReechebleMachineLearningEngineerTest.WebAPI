"""
A pay loan installment command handler module.
"""

import sys

from reecheble_finance.application.sdk.dtos.pay_loan_installment.pay_loan_installment_response_dto import (
    PayLoanInstallmentResponseDTO)
from reecheble_finance.application.services.abstract_service import AbstractApplicationService
from reecheble_finance.application.services.loan_service.pay_loan_installment.pay_loan_installment_command import (
    PayLoanInstallmentCommand)
from reecheble_finance.domain.abstract_repository.abstract_repository import RepositoryContextSession
from reecheble_finance.domain.enums.response_status.response_status import ResponseStatusEnum
from reecheble_finance.domain.models.loan_account import LoanAccount
from reecheble_finance.domain.models.loan_request import LoanRequest
from reecheble_finance.infrastructure.data_access.repositories.loan_account_repository.abstract_loan_account_repository import (
    AbstractLoanAccountRepository)
from reecheble_finance.infrastructure.data_access.repositories.loan_account_repository.loan_account_repository import (
    LoanAccountRepository)
from reecheble_finance.infrastructure.data_access.repositories.loan_repository.abstract_loan_repository import (
    AbstractLoanRepository)
from reecheble_finance.infrastructure.data_access.repositories.loan_repository.loan_repository import LoanRepository
from reecheble_finance.shared.result.result import Result, SuccessResult, FailureResult


class PayLoanInstallmentCommandHandler(AbstractApplicationService):

    def __init__(self, context: RepositoryContextSession) -> None:
        super().__init__(context=context)
        self.loan_repository: AbstractLoanRepository = LoanRepository(context=self.context)
        self.loan_account_repository: AbstractLoanAccountRepository = LoanAccountRepository(context=self.context)

    async def handle(self, command: PayLoanInstallmentCommand) -> Result[PayLoanInstallmentResponseDTO]:
        """
        Asynchronous pay loan installment command handler.

        :param command: Pay loan installment command.
        """

        try:
            loan_request: LoanRequest = self.loan_repository.get(id=command.data.loan_id)

            if loan_request.account.outstanding_balance == 0:
                return SuccessResult(data=PayLoanInstallmentResponseDTO(
                    loan_id=loan_request.id,
                    loan_outstanding_balance=0.00,
                    interest_paid=0.00,
                    principal_paid=0.00,
                    amount_paid=0.00),
                    status=ResponseStatusEnum.success,
                    message="This loan has been paid out. You can apply for a new loan on this account.")
            loan_request.make_payment()
            loan_account: LoanAccount = self.loan_account_repository.update(loan_account=loan_request.account)
            # update loan_request
            loan_request = self.loan_repository.update(loan_request=loan_request)

            return SuccessResult(data=PayLoanInstallmentResponseDTO(
                loan_id=loan_request.id,
                loan_outstanding_balance=loan_account.outstanding_balance,
                interest_paid=loan_request.latest_interest_paid,
                principal_paid=loan_request.latest_principal_paid,
                amount_paid=round(loan_request.latest_interest_paid + loan_request.latest_principal_paid, 2)),
                status=ResponseStatusEnum.success)

        except Exception as ex:
            print(f"Error: {ex}", file=sys.stderr)
            return FailureResult(data=None, status=ResponseStatusEnum.fail, message="That was definitely not expected")
