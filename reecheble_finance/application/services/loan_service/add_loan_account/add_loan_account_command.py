"""
A Reecheble Finance loan account creation command module.
"""
from reecheble_finance.application.sdk.dtos.add_loan_account.add_loan_account_request_dto import (
    AddLoanAccountRequestDTO)
from reecheble_finance.application.services.abstract_command import BaseCommand

__all__ = [
    "AddLoanAccountCommand",
]


class AddLoanAccountCommand(BaseCommand):
    """
    Reecheble Finance loan account creation command.

    :param data: Reecheble Finance loan account creation command details
    """

    data: AddLoanAccountRequestDTO
