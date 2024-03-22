"""
A loan application command handler module.
"""
import sys
import uuid

from reecheble_finance.application.sdk.dtos.add_loan_application.add_loan_application_response_dto import (
    AddLoanApplicationResponseDTO)
from reecheble_finance.application.services.abstract_service import AbstractApplicationService
from reecheble_finance.application.services.loan_service.add_loan.add_loan_application_command import (
    AddLoanApplicationCommand)
from reecheble_finance.domain.abstract_repository.abstract_repository import RepositoryContextSession
from reecheble_finance.domain.enums.response_status.response_status import ResponseStatusEnum
from reecheble_finance.domain.exceptions.domain_exceptions import LoanRequestDomainException
from reecheble_finance.domain.models.loan_account import LoanAccount
from reecheble_finance.domain.models.loan_request import LoanRequest
from reecheble_finance.infrastructure.data_access.repositories.loan_account_repository.abstract_loan_account_repository import (
    AbstractLoanAccountRepository)
from reecheble_finance.infrastructure.data_access.repositories.loan_account_repository.loan_account_repository import (
    LoanAccountRepository)
from reecheble_finance.infrastructure.data_access.repositories.loan_repository.abstract_loan_repository import (
    AbstractLoanRepository)
from reecheble_finance.infrastructure.data_access.repositories.loan_repository.loan_repository import LoanRepository
from reecheble_finance.shared.result.result import Result, FailureResult, SuccessResult


class AddLoanApplicationCommandHandler(AbstractApplicationService):

    def __init__(self, context: RepositoryContextSession) -> None:
        super().__init__(context=context)
        self.loan_repository: AbstractLoanRepository = LoanRepository(context=self.context)
        self.loan_account_repository: AbstractLoanAccountRepository = LoanAccountRepository(context=self.context)

    async def handle(self, command: AddLoanApplicationCommand) -> Result[AddLoanApplicationResponseDTO]:
        """
        Asynchronous loan application request handler.

        :param command: Loan application command
        """

        try:
            loan_account: LoanAccount = self.loan_account_repository.get(id=command.data.account_id)

            if loan_account is None:
                print(f"Loan account with id: {command.data.account_id} not found", file=sys.stderr)
                return FailureResult(data=None,
                                     message="That was definitely not expected",
                                     status=ResponseStatusEnum.fail)

            loan_request = LoanRequest(
                id=uuid.uuid4(),
                account=loan_account,
                interest_rate=command.data.interest_rate,
                payment_period_in_months=command.data.payment_period_in_months,
                request_amount=command.data.request_amount
            )
            loan_request.request_loan()
            self.loan_account_repository.update(loan_account=loan_account)
            loan: LoanRequest = self.loan_repository.add(request=loan_request)

            return SuccessResult(
                data=AddLoanApplicationResponseDTO(
                    id=loan.id,
                    loan_amount=loan.request_amount,
                    loan_granted=True,
                    equated_monthly_installment=loan.equated_monthly_installment,
                    loan_outstanding_balance=loan.account.outstanding_balance,
                    interest_paid=loan.latest_interest_paid,
                    principal_paid=loan.latest_principal_paid,
                    amount_paid=round(loan.latest_interest_paid + loan.latest_principal_paid, 2)),
                status=ResponseStatusEnum.success)

        except LoanRequestDomainException as ex:
            print(f"Error: {ex}", file=sys.stderr)
            return FailureResult(data=None,
                                 message="Come on, you still have a loan with an outstanding balance.",
                                 status=ResponseStatusEnum.fail)

        except Exception as ex:
            print(f"Error: {ex}", file=sys.stderr)
            return FailureResult(data=None,
                                 message="That was definitely not expected",
                                 status=ResponseStatusEnum.fail)
