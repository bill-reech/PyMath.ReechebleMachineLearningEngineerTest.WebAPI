from pydantic import EmailStr

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "AddLoanAccountRequestDTO"
]


class AddLoanAccountRequestDTO(BaseDomainParserMixin):
    first_name: str
    last_name: str
    email_address: EmailStr
