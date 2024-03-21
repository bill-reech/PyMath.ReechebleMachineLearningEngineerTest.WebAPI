"""
A loan application command handler module.
"""
from reecheble_finance.application.sdk.dtos.add_loan_application.add_loan_application_response_dto import (
    AddLoanApplicationResponseDTO)
from reecheble_finance.application.services.abstract_service import AbstractApplicationService
from reecheble_finance.application.services.loan_service.add_loan.add_loan_application_command import (
    AddLoanApplicationCommand)
from reecheble_finance.domain.abstract_repository.abstract_repository import RepositoryContextSession
from reecheble_finance.domain.models.loan_request import LoanRequest
from reecheble_finance.infrastructure.data_access.repositories.loan_repository.abstract_loan_repository import (
    AbstractLoanRepository)
from reecheble_finance.infrastructure.data_access.repositories.loan_repository.loan_repository import LoanRepository


class AddLoanApplicationCommandHandler(AbstractApplicationService):

    def __init__(self, context: RepositoryContextSession) -> None:
        super().__init__(context=context)
        self.repository: AbstractLoanRepository = LoanRepository(context=self.context)

    async def handle(self, command: AddLoanApplicationCommand) -> AddLoanApplicationResponseDTO:
        """
        Asynchronous loan application request handler.

        :param command: Loan application command
        """

        loan_request = LoanRequest(
            account=command.data.account,
            interest_rate=command.data.interest_rate,
            payment_period_in_months=command.data.payment_period_in_months,
            request_amount=command.data.request_amount
        )
        loan = self.repository.add(request=loan_request)
        return AddLoanApplicationResponseDTO(id=loan.id, loan_amount=loan_request.request_amount, loan_granted=True)
