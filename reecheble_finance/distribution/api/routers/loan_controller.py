from uuid import UUID

from fastapi import Depends, APIRouter
from fastapi_versioning import version

from reecheble_finance.application.sdk.dtos.add_loan_application.add_loan_application_request_dto import (
    AddLoanApplicationRequestDTO
)
from reecheble_finance.application.sdk.dtos.add_loan_application.add_loan_application_response_dto import (
    AddLoanApplicationResponseDTO
)
from reecheble_finance.application.services.loan_service.add_loan.add_loan_application_command import (
    AddLoanApplicationCommand
)
from reecheble_finance.application.services.loan_service.add_loan.add_loan_application_handler import (
    AddLoanApplicationCommandHandler
)
from reecheble_finance.distribution.api.dependencies import router_path_dependency
from reecheble_finance.infrastructure.data_access.database.databases_tools.contexts.context_types import (
    PyMongoDbContext
)
from reecheble_finance.infrastructure.data_access.repositories.loan_repository import LoanRepository

router = APIRouter(
    prefix="/loan",
    tags=["loan"],
    responses={404: {"description": "Not found"}}
)


@router.post(
    "/loan_application",
    name="Apply for a loan at Reecheble",
    status_code=200,
    response_model=AddLoanApplicationResponseDTO,
    description="Post a request to add a loan application.",
)
@version(0, 0)
async def add_loan_application(
        request: AddLoanApplicationRequestDTO,
        path_dependency: PyMongoDbContext = Depends(router_path_dependency)) -> AddLoanApplicationResponseDTO:
    with path_dependency.context().get_context() as context:
        return await AddLoanApplicationCommandHandler(
            context=context,
            repository=LoanRepository
        ).handle(command=AddLoanApplicationCommand(details=request))
