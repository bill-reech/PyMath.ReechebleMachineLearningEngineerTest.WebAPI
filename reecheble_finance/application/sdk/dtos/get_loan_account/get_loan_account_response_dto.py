from uuid import UUID

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "GetLoanAccountResponseDTO"
]


class GetLoanAccountResponseDTO(BaseDomainParserMixin):
    id: UUID
    account_number: str | None = None
    first_name: str
    last_name: str
    email_address: str
