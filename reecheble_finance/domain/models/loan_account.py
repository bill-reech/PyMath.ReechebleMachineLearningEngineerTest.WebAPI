import hashlib
import random
import string
import time
import uuid
from uuid import UUID

from pydantic import EmailStr, confloat, constr

from reecheble_finance.domain.abstract_domain import BaseDomainParserMixin


class LoanAccount(BaseDomainParserMixin):
    id: UUID
    account_number: constr(min_length=12, max_length=12)
    outstanding_balance: confloat(ge=0.00) = 0.00
    first_name: str
    last_name: str
    email_address: EmailStr

    @staticmethod
    def create_loan_account_number():
        salt = uuid.uuid4().hex
        hash_object = hashlib.sha256(salt.encode() + str(time.time()).encode())
        hex_dig = hash_object.hexdigest()
        random.seed(hex_dig)
        return "RF" + ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(10))
