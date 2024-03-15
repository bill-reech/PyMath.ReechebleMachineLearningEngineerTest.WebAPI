"""
A Reecheble Finance loan application command module.
"""

from reecheble_finance.application.sdk.dtos.add_loan_application.add_loan_application_request_dto import (
    AddLoanApplicationRequestDTO
)
from reecheble_finance.application.services.abstract_command import BaseCommand

__all__ = [
    "AddLoanApplicationCommand",
]


class AddLoanApplicationCommand(BaseCommand):
    """
    Reecheble Finance loan application command.

    :param details: Reecheble Finance loan application command details
    """

    details: AddLoanApplicationRequestDTO
