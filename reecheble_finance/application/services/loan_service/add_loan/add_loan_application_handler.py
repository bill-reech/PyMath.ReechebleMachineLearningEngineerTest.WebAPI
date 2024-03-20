"""
A loan application command handler module.
"""

from typing import Type

from reecheble_finance.domain.models.loan_request import LoanRequest
from reecheble_finance.application.services.abstract_service import AbstractApplicationService
from reecheble_finance.infrastructure.data_access.repositories.loan_repository.loan_repository import LoanRepository
from reecheble_finance.infrastructure.data_access.repositories.loan_repository.abstract_loan_repository import (
    AbstractLoanRepository)
from reecheble_finance.application.services.loan_service.add_loan.add_loan_application_command import (
    AddLoanApplicationCommand)
from reecheble_finance.application.sdk.dtos.add_loan_application.add_loan_application_response_dto import (
    AddLoanApplicationResponseDTO)


class AddLoanApplicationCommandHandler(AbstractApplicationService):

    def __init__(self, context, repository: Type[LoanRepository]) -> None:
        super().__init__(context=context)
        self.repository: LoanRepository = repository(context=self.context)

    async def handle(self, command: AddLoanApplicationCommand) -> AddLoanApplicationResponseDTO:
        """
        Asynchronous loan application request handler.

        :param command: Loan application command
        """

        loan_request = LoanRequest(
            account=command.details.account,
            interest_rate=command.details.interest_rate,
            payment_period_in_months=command.details.payment_period_in_months
        )
        loan = self.repository.add(request=loan_request)
        return AddLoanApplicationResponseDTO(id=loan.id)
