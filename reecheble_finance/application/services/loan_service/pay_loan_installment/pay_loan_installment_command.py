"""
A Reecheble Finance pay loan installment command module.
"""

from reecheble_finance.application.sdk.dtos.pay_loan_installment.pay_loan_installment_request_dto import \
    PayLoanInstallmentRequestDTO
from reecheble_finance.application.services.abstract_command import BaseCommand

__all__ = [
    "PayLoanInstallmentCommand"
]


class PayLoanInstallmentCommand(BaseCommand):
    """
     Reecheble Finance pay loan installment command.

     :param data: Reecheble Finance pay loan installment command details
     """
    data: PayLoanInstallmentRequestDTO
