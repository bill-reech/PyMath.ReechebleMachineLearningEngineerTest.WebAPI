from typing import Optional
from uuid import UUID

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin


class User(BaseDomainParserMixin):
    id: Optional[UUID]
    first_name: str
    last_name: str
