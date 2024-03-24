from typing import List

from fastapi import Depends, APIRouter
from fastapi_versioning import version

from reecheble_finance.application.sdk.dtos.add_loan_account.add_loan_account_request_dto import (
    AddLoanAccountRequestDTO)
from reecheble_finance.application.sdk.dtos.add_loan_account.add_loan_account_response_dto import (
    AddLoanAccountResponseDTO)
from reecheble_finance.application.sdk.dtos.get_loan_account.get_loan_account_request_dto import (
    GetLoanAccountRequestDTO)
from reecheble_finance.application.sdk.dtos.get_loan_account.get_loan_account_response_dto import (
    GetLoanAccountResponseDTO)
from reecheble_finance.application.services.loan_service.add_loan_account.add_loan_account_command import (
    AddLoanAccountCommand)
from reecheble_finance.application.services.loan_service.add_loan_account.add_loan_account_command_handler import (
    AddLoanAccountCommandHandler)
from reecheble_finance.application.services.loan_service.get_loan_account.get_loan_accounts_query import (
    GetLoanAccountsQuery)
from reecheble_finance.application.services.loan_service.get_loan_account.get_loan_accounts_query_handler import (
    GetLoanAccountsQueryHandler)
from reecheble_finance.distribution.api.dependencies import router_path_dependency
from reecheble_finance.infrastructure.data_access.database.databases_tools.contexts.context_types import (
    PyMongoDbContext)
from reecheble_finance.shared.result.result import Result

router = APIRouter(
    prefix="/account",
    tags=["account"],
    responses={404: {"description": "Not found"}}
)


@router.post(
    "/add_account",
    name="Add a loan account to Reecheble",
    status_code=200,
    response_model=Result[AddLoanAccountResponseDTO],
    description="Post a request to add a loan account.",
)
@version(0, 0)
async def add_loan_account(
        request: AddLoanAccountRequestDTO,
        path_dependency: PyMongoDbContext = Depends(router_path_dependency)) -> Result[AddLoanAccountResponseDTO]:
    with path_dependency.context().get_context() as context:
        add_loan_account_handler = AddLoanAccountCommandHandler(context=context)
        return await add_loan_account_handler.handle(command=AddLoanAccountCommand(data=request))


@router.get(
    "/all_accounts",
    name="Get all loan accounts opened at Reecheble",
    status_code=200,
    response_model=Result[List[GetLoanAccountResponseDTO]],
    description="Get all loan accounts opened at Reecheble.",
)
@version(0, 1)
async def get_loan_accounts(
        path_dependency: PyMongoDbContext = Depends(router_path_dependency)) -> Result[List[GetLoanAccountResponseDTO]]:
    with path_dependency.context().get_context() as context:
        add_loan_account_handler = GetLoanAccountsQueryHandler(context=context)
        return await add_loan_account_handler.handle(query=GetLoanAccountsQuery(data=GetLoanAccountRequestDTO()))
