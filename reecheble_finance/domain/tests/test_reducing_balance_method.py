import uuid
from unittest.mock import patch

import pytest
from dateutil.relativedelta import relativedelta
from faker import Faker
from hypothesis import given
from hypothesis.strategies import floats, integers, builds, just

from reecheble_finance.domain.exceptions.domain_exceptions import LoanRequestDomainException
from reecheble_finance.domain.models.loan_account import LoanAccount
from reecheble_finance.domain.models.loan_request import LoanRequest

fake = Faker()


def fake_first_name():
    return fake.first_name()


def fake_last_name():
    return fake.last_name()


def fake_email_address():
    return fake.email()


def fake_guid():
    return uuid.uuid4()


# Define the strategy for generating random user and account models.
user_account_strategy = builds(
    LoanAccount,
    id=just(fake_guid()),
    first_name=just(fake_first_name()),
    last_name=just(fake_last_name()),
    email_address=just(fake_email_address())
)


@given(account_balance=floats(min_value=0.01, max_value=5000),
       interest_rate=floats(min_value=0.05, max_value=0.5),
       payment_period=integers(min_value=3, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_valid_loan_request_then_user_can_not_take_loan_with_outstanding_balance_on_previous_loan(
        account_balance,
        interest_rate,
        payment_period,
        loan_amount,
        account_model):

    # Arrange
    account_model.outstanding_balance = account_balance

    # Assert & Act
    with (pytest.raises(LoanRequestDomainException)):
        LoanRequest(
            id=uuid.uuid4(),
            account=account_model,
            interest_rate=interest_rate,
            payment_period_in_months=payment_period,
            request_amount=loan_amount).request_loan()


@given(interest_rate=floats(min_value=0.05, max_value=0.5),
       payment_period=integers(min_value=3, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_valid_loan_request_then_a_new_loan_is_added_to_user_account(
        interest_rate,
        payment_period,
        loan_amount,
        account_model):
    # Act
    LoanRequest(
        id=uuid.uuid4(),
        account=account_model,
        interest_rate=interest_rate,
        payment_period_in_months=payment_period,
        request_amount=loan_amount
    ).request_loan()

    # Assert
    assert account_model.outstanding_balance == round(loan_amount, 2)


@given(interest_rate=floats(min_value=0.05, max_value=0.5),
       payment_period=integers(min_value=12, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_valid_loan_request_then_emi_should_be_set_for_the_loan(
        interest_rate,
        payment_period,
        loan_amount,
        account_model):

    # Act
    loan_request = LoanRequest(
        id=uuid.uuid4(),
        account=account_model,
        interest_rate=interest_rate,
        payment_period_in_months=payment_period,
        request_amount=loan_amount)
    loan_request.request_loan()
    emi = LoanRequest.get_equated_monthly_installment(
        loan_amount=loan_amount,
        monthly_interest_rate=interest_rate,
        number_of_installments=payment_period)

    # Assert
    assert loan_request.equated_monthly_installment == emi


@given(interest_rate=floats(min_value=0.05, max_value=0.5),
       payment_period=integers(min_value=12, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_valid_loan_repayment_request_then_the_current_balance_reduces_by_principal_amount_paid(
        interest_rate,
        payment_period,
        loan_amount,
        account_model):

    # Act
    loan_request = LoanRequest(
        id=uuid.uuid4(),
        account=account_model,
        interest_rate=interest_rate,
        payment_period_in_months=payment_period,
        request_amount=loan_amount)
    loan_request.request_loan()
    initial_balance = account_model.outstanding_balance
    loan_request.make_payment()

    # Assert
    assert round(account_model.outstanding_balance, 2) == round(initial_balance - loan_request.latest_principal_paid, 2)


@given(interest_rate=floats(min_value=0.05, max_value=0.5),
       payment_period=integers(min_value=12, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_valid_loan_repayment_the_the_payment_schedule_start_interest_amount_paid_is_zero(
        interest_rate,
        payment_period,
        loan_amount,
        account_model):
    loan_request = LoanRequest(
        id=uuid.uuid4(),
        account=account_model,
        interest_rate=interest_rate,
        payment_period_in_months=payment_period,
        request_amount=loan_amount)
    loan_request.request_loan()
    assert loan_request.latest_interest_paid == 0.00


@given(interest_rate=floats(min_value=0.05, max_value=0.5),
       payment_period=integers(min_value=12, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_valid_loan_repayment_then_the_payment_schedule_start_principal_amount_paid_is_zero(
        interest_rate,
        payment_period,
        loan_amount,
        account_model):
    loan_request = LoanRequest(
        id=uuid.uuid4(),
        account=account_model,
        interest_rate=interest_rate,
        payment_period_in_months=payment_period,
        request_amount=loan_amount)
    loan_request.request_loan()
    assert loan_request.latest_principal_paid == 0.00


@given(interest_rate=floats(min_value=0.05, max_value=0.68),
       payment_period=integers(min_value=3, max_value=60),
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_two_consecutive_valid_loan_repayments_then_loan_balance_reduces_by_sum_of_the_two_consecutive_principals(
        interest_rate,
        payment_period,
        loan_amount,
        account_model):

    # Arrange
    loan_request = LoanRequest(
        id=uuid.uuid4(),
        account=account_model,
        interest_rate=interest_rate,
        payment_period_in_months=payment_period,
        request_amount=loan_amount)

    # Act
    loan_request.request_loan()

    # payment 1
    loan_request.make_payment()

    # payment 2
    loan_request.make_payment()

    last_principal_paid = loan_request.repayment_history[-1].principal_paid
    second_last_principal_paid = loan_request.repayment_history[-2].principal_paid
    loan_reference_balance = loan_request.repayment_history[-3].loan_balance
    balance_from_paid_principal = loan_reference_balance - sum([last_principal_paid, second_last_principal_paid])

    # Assert
    assert round(loan_request.account.outstanding_balance, 2) == round(balance_from_paid_principal, 2)


@given(interest_rate=floats(min_value=0.05, max_value=0.68),
       payment_period=integers(min_value=12, max_value=60),
       overdue_period=integers(min_value=1, max_value=50),
       loan_amount=floats(min_value=5000, max_value=100000),
       account_model=user_account_strategy)
def test_given_loan_duration_has_lapsed_then_no_interest_is_applied_on_outstanding_balance(
        interest_rate,
        payment_period,
        overdue_period,
        loan_amount,
        account_model):

    # Arrange
    loan_request = LoanRequest(
        id=uuid.uuid4(),
        account=account_model,
        interest_rate=interest_rate,
        payment_period_in_months=payment_period,
        request_amount=loan_amount)
    loan_request.request_loan()
    loan_due_date = loan_request.origination_date + relativedelta(months=+payment_period)

    with patch(".".join([LoanRequest.__module__, "date"])) as mock_date:
        mock_date.today.return_value = loan_due_date + relativedelta(months=overdue_period)

        # Act
        interest_amount_after_loan_due_date = loan_request.get_interest_on_balance(
            balance=loan_request.account.outstanding_balance)

        # Assert
        assert interest_amount_after_loan_due_date == 0.00
