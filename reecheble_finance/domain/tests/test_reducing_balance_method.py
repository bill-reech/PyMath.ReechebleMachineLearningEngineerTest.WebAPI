import pytest
from hypothesis import given
from hypothesis.strategies import floats, integers

from reecheble_finance.domain.exceptions.domain_exceptions import InvalidLoanRequestDomainException
from reecheble_finance.domain.models.account import Account
from reecheble_finance.domain.models.loan_request import LoanRequest
from reecheble_finance.domain.models.user import User


@given(account_balance=floats(min_value=0.01, max_value=5000),
       interest_rate=floats(min_value=0.05, max_value=0.5),
       payment_period=integers(min_value=3, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000))
def test_given_valid_loan_request_can_not_take_loan_with_outstanding_balance(
        account_balance,
        interest_rate,
        payment_period,
        loan_amount):

    # Arrange
    user_model = User(first_name="John", last_name="Doe")
    account_model = Account(user=user_model)
    account_model.outstanding_balance = account_balance

    # Assert & Act
    with (pytest.raises(InvalidLoanRequestDomainException)):
        LoanRequest(
            account=account_model,
            interest_rate=interest_rate,
            payment_period_in_months=payment_period
        ).request_loan(loan_amount)


@given(interest_rate=floats(min_value=0.05, max_value=0.5),
       payment_period=integers(min_value=3, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000))
def test_given_valid_loan_request_adds_a_new_loan_to_account(interest_rate, payment_period, loan_amount):

    # Arrange
    user_model = User(first_name="Zanele", last_name="Mokoena")
    account_model = Account(user=user_model)

    # Act
    LoanRequest(
        account=account_model,
        interest_rate=interest_rate,
        payment_period_in_months=payment_period
    ).request_loan(request_amount=loan_amount)

    # Assert
    assert account_model.outstanding_balance == loan_amount


@given(interest_rate=floats(min_value=0.05, max_value=0.5),
       payment_period=integers(min_value=12, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000))
def test_given_valid_loan_request_emi_property_set(interest_rate, payment_period, loan_amount):
    # Arrange
    user_model = User(first_name="Kobus", last_name="Ndlovu")
    account_model = Account(user=user_model)

    # Act
    loan_request = LoanRequest(
        account=account_model,
        interest_rate=interest_rate,
        payment_period_in_months=payment_period)
    loan_request.request_loan(request_amount=loan_amount)
    emi = LoanRequest.get_equated_monthly_installment(
        loan_amount=loan_amount,
        monthly_interest_rate=interest_rate,
        number_of_installments=payment_period)

    # Assert
    assert loan_request.equated_monthly_instalment == emi


@given(interest_rate=floats(min_value=0.05, max_value=0.5),
       payment_period=integers(min_value=12, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000))
def test_given_valid_loan_repayment_request_current_balance_reduces_by_principal_paid(interest_rate, payment_period, loan_amount):
    # Arrange
    user_model = User(first_name="Sanele", last_name="Klass")
    account_model = Account(user=user_model)

    # Act
    loan_request = LoanRequest(
        account=account_model,
        interest_rate=interest_rate,
        payment_period_in_months=payment_period)
    loan_request.request_loan(request_amount=loan_amount)
    initial_balance = account_model.outstanding_balance
    loan_request.make_payment(balance=initial_balance)

    # Assert
    assert account_model.outstanding_balance == initial_balance - loan_request.principal_paid
