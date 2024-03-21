from uuid import UUID

from pydantic import EmailStr, confloat

from reecheble_finance.domain.abstract_domain import BaseDomainParserMixin


class LoanAccount(BaseDomainParserMixin):
    id: UUID
    outstanding_balance: confloat(ge=0.00) = 0.00
    first_name: str
    last_name: str
    email_address: EmailStr
