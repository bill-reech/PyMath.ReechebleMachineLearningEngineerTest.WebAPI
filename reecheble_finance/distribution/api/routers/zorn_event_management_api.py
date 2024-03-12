from uuid import UUID

from fastapi import Depends, APIRouter
from fastapi_versioning import version

from reecheble_finance.distribution.api.dependencies import router_path_dependency
from reecheble_finance.application.sdk.dtos.zorn_event_request.request_dto import ZornEventRequestDTO
from reecheble_finance.infrastructure.data_access.database.databases_tools.contexts.context_types import SqlAlchemyContext
from reecheble_finance.infrastructure.data_access.repositories.zorn_event_management_repository import ZornEventManagementRepository
from reecheble_finance.application.services.zorn_event_management_service.create_zorn_event.create_zorn_event_command import (
    CreateZornEventCommand)
from reecheble_finance.application.services.zorn_event_management_service.create_zorn_event.create_zorn_event_command_handler import (
    CreateZornEventCommandHandler)


router = APIRouter(
    prefix="/zorn_event_manager",
    tags=["zorn_event_manager"],
    responses={404: {"description": "Not found"}}
)


@router.post(
    "/create_zorn_event",
    name="Create zoRn event",
    status_code=200,
    response_model=UUID,
    description="Post a request to create a zoRn Event.",
)
@version(0, 0)
async def create_zorn_event_request(
        request: ZornEventRequestDTO,
        path_dependency: SqlAlchemyContext = Depends(router_path_dependency)) -> UUID:
    with path_dependency.context().get_context() as context:
        return await CreateZornEventCommandHandler(
            context=context,
            repository=ZornEventManagementRepository
        ).handle(command=CreateZornEventCommand(details=request))
