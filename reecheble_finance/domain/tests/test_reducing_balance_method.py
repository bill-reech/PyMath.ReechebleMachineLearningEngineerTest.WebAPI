import pytest

from reecheble_finance.domain.exceptions.domain_exceptions import InvalidLoanRequestDomainException
from reecheble_finance.domain.models.account import Account
from reecheble_finance.domain.models.loan_request import LoanRequest
from reecheble_finance.domain.models.user import User


def test_given_valid_loan_request_can_not_take_loan_with_outstanding_balance():
    user_model = User(first_name="Mduduzi", last_name="Mlilo")
    account_model = Account(user=user_model)
    account_model.outstanding_balance = 1000

    with pytest.raises(InvalidLoanRequestDomainException):
        loan_request = LoanRequest(account=account_model, interest_rate=0.1, payment_period_in_months=18)
        loan_request.request_loan(100000)


def test_given_valid_loan_request_adds_a_new_loan_to_account():
    user_model = User(first_name="Mduduzi", last_name="Mlilo")
    account_model = Account(user=user_model)
    loan_request = LoanRequest(account=account_model, interest_rate=0.1, payment_period_in_months=18)
    loan_request.request_loan(request_amount=100000)
    assert account_model.outstanding_balance == 100000


def test_given_valid_loan_request_emi_property_set():
    user_model = User(first_name="Mduduzi", last_name="Mlilo")
    account_model = Account(user=user_model)
    loan_request = LoanRequest(account=account_model, interest_rate=0.1, payment_period_in_months=18)
    loan_request.request_loan(request_amount=100000)
    assert loan_request.equated_monthly_instalment == LoanRequest.get_equated_monthly_installment(loan_amount=100000, monthly_interest_rate=0.1, number_of_installments=18)
