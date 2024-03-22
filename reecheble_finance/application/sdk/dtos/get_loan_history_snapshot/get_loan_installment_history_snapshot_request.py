from uuid import UUID

from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "GetLoanInstallmentHistorySnapshotRequestDTO"
]


class GetLoanInstallmentHistorySnapshotRequestDTO(BaseDomainParserMixin):
    id: UUID
