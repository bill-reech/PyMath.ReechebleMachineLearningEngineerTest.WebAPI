from fastapi import Depends, APIRouter
from fastapi_versioning import version

from reecheble_finance.application.sdk.dtos.add_loan_application.add_loan_application_request_dto import (
    AddLoanApplicationRequestDTO)
from reecheble_finance.application.sdk.dtos.add_loan_application.add_loan_application_response_dto import (
    AddLoanApplicationResponseDTO)
from reecheble_finance.application.sdk.dtos.pay_loan_installment.pay_loan_installment_request_dto import (
    PayLoanInstallmentRequestDTO)
from reecheble_finance.application.sdk.dtos.pay_loan_installment.pay_loan_installment_response_dto import (
    PayLoanInstallmentResponseDTO)
from reecheble_finance.application.services.loan_service.add_loan.add_loan_application_command import (
    AddLoanApplicationCommand)
from reecheble_finance.application.services.loan_service.add_loan.add_loan_application_handler import (
    AddLoanApplicationCommandHandler)
from reecheble_finance.application.services.loan_service.pay_loan_installment.pay_loan_installment_command import (
    PayLoanInstallmentCommand)
from reecheble_finance.application.services.loan_service.pay_loan_installment.pay_loan_installment_handler import (
    PayLoanInstallmentCommandHandler)
from reecheble_finance.distribution.api.dependencies import router_path_dependency
from reecheble_finance.infrastructure.data_access.database.databases_tools.contexts.context_types import (
    PyMongoDbContext)
from reecheble_finance.shared.result.result import Result

router = APIRouter(
    prefix="/loan",
    tags=["loan"],
    responses={404: {"description": "Not found"}}
)


@router.post(
    "/add_loan",
    name="Apply for a loan at Reecheble",
    status_code=200,
    response_model=Result[AddLoanApplicationResponseDTO],
    description="Post a request to add a loan application. "
                "A loan account must be created first before putting a loan application.",
)
@version(0, 1)
async def add_loan_application(
        request: AddLoanApplicationRequestDTO,
        path_dependency: PyMongoDbContext = Depends(router_path_dependency)) -> Result[AddLoanApplicationResponseDTO]:
    with path_dependency.context().get_context() as context:
        add_loan_application_handler = AddLoanApplicationCommandHandler(context=context)
        return await add_loan_application_handler.handle(command=AddLoanApplicationCommand(data=request))


@router.post(
    "/pay_loan",
    name="Pay a loan installment at Reecheble",
    status_code=200,
    response_model=Result[PayLoanInstallmentResponseDTO],
    description="Post a request to pay a loan installment. "
                "A loan must be created first before paying a loan installment.",
)
@version(0, 1)
async def pay_loan_installment(
        request: PayLoanInstallmentRequestDTO,
        path_dependency: PyMongoDbContext = Depends(router_path_dependency)) -> Result[PayLoanInstallmentResponseDTO]:
    with path_dependency.context().get_context() as context:
        pay_loan_installment_handler = PayLoanInstallmentCommandHandler(context=context)
        return await pay_loan_installment_handler.handle(command=PayLoanInstallmentCommand(data=request))
