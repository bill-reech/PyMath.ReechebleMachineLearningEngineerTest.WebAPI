from uuid import UUID

from pydantic import EmailStr, constr

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "AddLoanAccountResponseDTO"
]


class AddLoanAccountResponseDTO(BaseDomainParserMixin):
    id: UUID
    account_number: constr(min_length=12, max_length=12)
    first_name: str
    last_name: str
    email_address: EmailStr
