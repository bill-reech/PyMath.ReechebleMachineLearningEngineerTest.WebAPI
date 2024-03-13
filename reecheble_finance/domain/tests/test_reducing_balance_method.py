import pytest
from faker import Faker
from hypothesis import given
from hypothesis.strategies import floats, integers, builds, just

from reecheble_finance.domain.exceptions.domain_exceptions import InvalidLoanRequestDomainException
from reecheble_finance.domain.models.account import Account
from reecheble_finance.domain.models.loan_request import LoanRequest
from reecheble_finance.domain.models.user import User

fake = Faker()


def fake_first_name():
    return fake.first_name()


def fake_last_name():
    return fake.last_name()


# Define the strategy for generating random user and account models.
user_account_strategy = builds(
    Account,
    user=builds(
        User,
        first_name=just(fake_first_name()),
        last_name=just(fake_last_name())
    )
)


@given(account_balance=floats(min_value=0.01, max_value=5000),
       interest_rate=floats(min_value=0.05, max_value=0.5),
       payment_period=integers(min_value=3, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_valid_loan_request_can_not_take_loan_with_outstanding_balance(
        account_balance,
        interest_rate,
        payment_period,
        loan_amount,
        account_model):

    # Arrange
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
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_valid_loan_request_adds_a_new_loan_to_account(interest_rate, payment_period, loan_amount, account_model):
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
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_valid_loan_request_emi_property_set(interest_rate, payment_period, loan_amount, account_model):

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
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_valid_loan_repayment_request_current_balance_reduces_by_principal_paid(
        interest_rate,
        payment_period,
        loan_amount,
        account_model):

    # Act
    loan_request = LoanRequest(
        account=account_model,
        interest_rate=interest_rate,
        payment_period_in_months=payment_period)
    loan_request.request_loan(request_amount=loan_amount)
    initial_balance = account_model.outstanding_balance
    loan_request.make_payment()

    # Assert
    assert account_model.outstanding_balance == initial_balance - loan_request.principal_paid


@given(interest_rate=floats(min_value=0.05, max_value=0.5),
       payment_period=integers(min_value=12, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_valid_loan_repayment_the_payment_schedule_start_interest_paid_amount_is_zero(
        interest_rate,
        payment_period,
        loan_amount,
        account_model):
    loan_request = LoanRequest(
        account=account_model,
        interest_rate=interest_rate,
        payment_period_in_months=payment_period)
    loan_request.request_loan(request_amount=loan_amount)
    assert loan_request.interest_paid == 0.00


@given(interest_rate=floats(min_value=0.05, max_value=0.5),
       payment_period=integers(min_value=12, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_valid_loan_repayment_the_payment_schedule_start_principal_paid_amount_is_zero(
        interest_rate,
        payment_period,
        loan_amount,
        account_model):
    loan_request = LoanRequest(
        account=account_model,
        interest_rate=interest_rate,
        payment_period_in_months=payment_period)
    loan_request.request_loan(request_amount=loan_amount)
    assert loan_request.principal_paid == 0.00


@given(interest_rate=floats(min_value=0.05, max_value=0.68),
       payment_period=integers(min_value=12, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_two_consecutive_valid_loan_repayments_loan_balance_reduces_by_sum_of_the_two_consecutive_principals(
        interest_rate,
        payment_period,
        loan_amount,
        account_model):

    # Arrange
    loan_request = LoanRequest(
        account=account_model,
        interest_rate=interest_rate,
        payment_period_in_months=payment_period)

    # Act
    loan_request.request_loan(request_amount=loan_amount)

    # payment 1
    loan_request.make_payment()

    # payment 2
    loan_request.make_payment()

    last_principal_paid = loan_request.repayment_history[-1].principal_paid
    second_last_principal_paid = loan_request.repayment_history[-2].principal_paid
    loan_reference_balance = loan_request.repayment_history[-3].loan_balance
    balance_from_paid_principal = loan_reference_balance - sum([last_principal_paid, second_last_principal_paid])

    # Assert
    assert loan_request.account.outstanding_balance == balance_from_paid_principal
