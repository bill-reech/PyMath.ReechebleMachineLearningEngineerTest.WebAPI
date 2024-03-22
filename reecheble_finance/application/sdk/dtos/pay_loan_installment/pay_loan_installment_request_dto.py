from uuid import UUID

from pydantic import confloat

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "PayLoanInstallmentRequestDTO"
]


class PayLoanInstallmentRequestDTO(BaseDomainParserMixin):
    loan_id: UUID
    installment_amount: confloat(ge=0)
