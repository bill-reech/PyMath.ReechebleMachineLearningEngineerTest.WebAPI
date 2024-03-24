from reecheble_finance.application.sdk.dtos.get_loan_account.get_loan_account_request_dto import (
    GetLoanAccountRequestDTO)
from reecheble_finance.application.services.abstract_query import BaseQuery

__all__ = [
    "GetLoanAccountsQuery"
]


class GetLoanAccountsQuery(BaseQuery):
    data: GetLoanAccountRequestDTO
