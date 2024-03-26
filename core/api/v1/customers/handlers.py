from django.http import HttpRequest

from ninja import Router
from ninja.errors import HttpError

from core.api.schemas import ApiResponse
from core.api.v1.customers.schemas import (
    AuthInSchema,
    AuthOutSchema,
    TokenInSchema,
    TokenOutSchema,
)
from core.apps.common.exceptions import ServiceException
from core.apps.customers.services.auth import AuthService
from core.apps.customers.services.codes import DjangoCacheCodeService
from core.apps.customers.services.customers import ORMCustomerService
from core.apps.customers.services.sender import DummySenderService


router = Router(tags=["Customers"])


@router.post("auth", response=ApiResponse[AuthOutSchema], operation_id="authorize")
def auth_handler(
    request: HttpRequest,
    auth_in_schema: AuthInSchema,
):
    auth_service = AuthService(
        customer_service=ORMCustomerService(),
        code_service=DjangoCacheCodeService(),
        sender_service=DummySenderService(),
    )
    auth_service.authorize(auth_in_schema.phone)
    return ApiResponse(
        data=AuthOutSchema(
            message=f"Code has been sent to {auth_in_schema.phone}",
        ),
    )


@router.post("confirm", response=ApiResponse[TokenOutSchema], operation_id="confirm_code")
def get_token_handler(
    request: HttpRequest,
    token_in_schema: TokenInSchema,
):
    auth_service = AuthService(
        customer_service=ORMCustomerService(),
        code_service=DjangoCacheCodeService(),
        sender_service=DummySenderService(),
    )

    try:
        token = auth_service.confirm(token_in_schema.code, token_in_schema.phone)
    except ServiceException as exception:
        raise HttpError(
            status_code=400,
            message="Не могу вывести эксепшн нормально",
        ) from exception

    return ApiResponse(data=TokenOutSchema(token=token))
