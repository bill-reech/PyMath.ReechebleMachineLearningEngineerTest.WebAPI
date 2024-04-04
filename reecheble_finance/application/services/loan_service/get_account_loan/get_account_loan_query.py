from reecheble_finance.application.sdk.dtos.get_account_loan.get_account_loan_request_dto import (
    GetAccountLoanRequestDTO)
from reecheble_finance.application.services.abstract_query import BaseQuery

__all__ = [
    "GetAccountLoanQuery"
]


class GetAccountLoanQuery(BaseQuery):
    data: GetAccountLoanRequestDTO
