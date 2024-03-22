from typing import (
    Any,
    Generic,
    List,
    TypeVar,
)

from ninja import Schema
from pydantic import Field

from core.api.filters import PaginationOut


TListItem = TypeVar("TListItem")
TData = TypeVar("TData")


class PingResponseSchema(Schema):
    result: bool


class ListPaginatedResponse(Schema, Generic[TListItem]):
    items: List[TListItem]
    pagination: PaginationOut


class ApiResponse(Schema, Generic[TData]):
    data: TData | dict = Field(default_factory=dict)
    meta: dict[str, Any] | dict = Field(default_factory=dict)
    errors: List[Any] | dict = Field(default_factory=dict)
