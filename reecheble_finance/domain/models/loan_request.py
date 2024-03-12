import math
from typing import Optional
from uuid import UUID

from pydantic import PositiveInt, PositiveFloat


from reecheble_finance.domain.exceptions.domain_exceptions import InvalidLoanRequestDomainException
from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin
from reecheble_finance.domain.models.account import Account

__all__ = [
    "LoanRequest"
]


class LoanRequest(BaseDomainParserMixin):
    id: Optional[UUID]
    account: Account
    request_amount: PositiveInt = 0
    interest_rate: float
    payment_period_in_months: PositiveInt
    equated_monthly_instalment: PositiveFloat = 0.00
    principal_paid: PositiveFloat = 0.00
    interest_paid: PositiveFloat = 0.00

    def request_loan(self, request_amount: int) -> None:
        """

        :param request_amount: Loan amount being requested
        :throws InvalidLoanRequestDomainException:
        """
        if self.account.outstanding_balance > 0.00:
            raise InvalidLoanRequestDomainException(message="Account has an outstanding balance")

        if self.account.outstanding_balance is None or self.account.outstanding_balance == 0:
            self.account.outstanding_balance = request_amount

        self.equated_monthly_instalment = self.get_equated_monthly_installment(
            loan_amount=request_amount,
            monthly_interest_rate=self.interest_rate,
            number_of_installments=self.payment_period_in_months)

    @staticmethod
    def get_equated_monthly_installment(
            loan_amount: int,
            monthly_interest_rate: float,
            number_of_installments: int) -> float:
        """
        Get the Equated Monthly Installment for a given loan amount borrowed at a specific interest rate
        over a specified time in months.

        :param loan_amount:
        :param monthly_interest_rate:
        :param number_of_installments:
        :return:
        :rtype: float
        """
        numerator = (loan_amount * monthly_interest_rate * math.pow(1 + monthly_interest_rate, number_of_installments))
        denominator = math.pow(1 + monthly_interest_rate, number_of_installments) - 1

        return numerator / denominator

    def get_interest_on_balance(self, balance: int) -> float:
        """

        :param balance:
        :return:
        :rtype: float
        """
        return balance * self.interest_rate / 12

    def make_payment(self, amount: int, balance: int) -> None:
        self.interest_paid = self.get_interest_on_balance(balance)

        if amount < self.interest_paid:
            ...
        self.principal_paid = self.equated_monthly_instalment - self.principal_paid
