from typing import Optional
from uuid import UUID

from pydantic import PositiveFloat

from reecheble_finance.domain.abstract_domain import BaseDomainParserMixin


class LoanAccount(BaseDomainParserMixin):
    id: Optional[UUID]
    outstanding_balance: PositiveFloat = 0.00
