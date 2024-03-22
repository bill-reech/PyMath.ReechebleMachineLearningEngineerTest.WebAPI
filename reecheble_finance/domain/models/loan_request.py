import math
import uuid
from datetime import date
from typing import List
from uuid import UUID

from dateutil.relativedelta import relativedelta
from pydantic import PositiveInt, confloat

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin
from reecheble_finance.domain.exceptions.domain_exceptions import LoanRequestDomainException
from reecheble_finance.domain.models.loan_account import LoanAccount
from reecheble_finance.domain.models.repayment_history import RepaymentHistory

__all__ = [
    "LoanRequest"
]


class LoanRequest(BaseDomainParserMixin):
    id: UUID
    account: LoanAccount
    request_amount: confloat(ge=0)
    interest_rate: confloat(ge=0, le=100)
    payment_period_in_months: PositiveInt
    origination_date: date = date.today()
    due_date: date = None
    equated_monthly_installment: confloat(ge=0.00) = 0.00
    latest_principal_paid: confloat(ge=0.00) = 0.00
    latest_interest_paid: confloat(ge=0.00) = 0.00
    repayment_history: List[RepaymentHistory] = []

    def request_loan(self) -> None:
        """
        Method: request_loan

        Description:
        Request a loan by specifying the loan amount.

        Raises:
            InvalidLoanRequestDomainException: If the account has an outstanding balance.

        Returns:
            None
        """
        if self.account.outstanding_balance > 0.00:
            raise LoanRequestDomainException(message="Account has an outstanding balance")

        if self.account.outstanding_balance is None or self.account.outstanding_balance == 0:
            self.account.outstanding_balance = self.request_amount

        self.equated_monthly_installment = self.get_equated_monthly_installment(
            loan_amount=self.request_amount,
            monthly_interest_rate=self.interest_rate,
            number_of_installments=self.payment_period_in_months)
        self.due_date = self.origination_date + relativedelta(months=+self.payment_period_in_months)

        self.repayment_history.append(
            RepaymentHistory(id=uuid.uuid4(), month=0, loan_balance=self.account.outstanding_balance))

    @staticmethod
    def get_equated_monthly_installment(
            loan_amount: float,
            monthly_interest_rate: float,
            number_of_installments: int) -> float:
        """
        Method: get_equated_monthly_installment

        Description:
        Get the Equated Monthly Installment for a given loan amount borrowed at a specific interest rate
        over a specified time in months.

        Parameters:
            loan_amount (float): The amount of money requested for the loan.
            monthly_interest_rate (float): Interest rate charged on the loan amount borrowed.
            number_of_installments (int): Number of installments stated on the loan agreement to amortise the loan.

        Returns:
            float: The equated monthly installment for a given loan amount borrowed.
        """
        numerator = (loan_amount * (monthly_interest_rate * 0.01 / 12) * math.pow(
            1 + (monthly_interest_rate * 0.01 / 12), number_of_installments))
        denominator = math.pow(1 + (monthly_interest_rate * 0.01 / 12), number_of_installments) - 1

        return numerator / denominator

    def get_interest_on_balance(self, balance: float) -> float:
        """
        Method: get_interest_on_balance

        Description:
        Calculate the interest on the specified balance based on the given interest rate.

        Parameters:
            balance (float): The balance for which the interest amount needs to be calculated.

        Returns:
            float: The calculated interest for the supplied balance given the interest rate.
        """

        if LoanRequest.set_loan_origination_date() > self.due_date:
            return 0.00  # Do not charge interest on overdue loans
        return balance * (self.interest_rate * 0.01) / self.payment_period_in_months

    def make_payment(self) -> None:
        """
        Method: make_payment

        Description:
        Make a payment towards the outstanding balance of the account.

        Returns:
            None:
        """
        self.latest_interest_paid = self.get_interest_on_balance(self.account.outstanding_balance)
        self.latest_principal_paid = self.equated_monthly_installment - self.latest_interest_paid
        if self.account.outstanding_balance < self.equated_monthly_installment:
            self.account.outstanding_balance = 0.00
        else:
            self.account.outstanding_balance -= self.latest_principal_paid
        self.repayment_history.append(
            RepaymentHistory(id=uuid.uuid4(),
                             month=len(self.repayment_history),
                             equated_monthly_instalment=self.equated_monthly_installment,
                             principal_paid=self.latest_principal_paid,
                             interest_paid=self.latest_interest_paid,
                             loan_balance=self.account.outstanding_balance)
        )

    @staticmethod
    def set_loan_origination_date():
        return date.today()
