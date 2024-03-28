from pydantic import confloat, constr

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "PayLoanInstallmentRequestDTO"
]


class PayLoanInstallmentRequestDTO(BaseDomainParserMixin):
    reference: constr(min_length=16, max_length=16)
    installment_amount: confloat(ge=0)
