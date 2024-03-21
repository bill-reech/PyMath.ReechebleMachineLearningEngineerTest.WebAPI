from uuid import UUID

from pydantic import confloat

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "AddLoanApplicationResponseDTO"
]


class AddLoanApplicationResponseDTO(BaseDomainParserMixin):
    id: UUID
    loan_amount: confloat(ge=0)
    loan_granted: bool
