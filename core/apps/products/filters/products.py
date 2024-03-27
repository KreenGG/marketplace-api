from dataclasses import dataclass

from pydantic import BaseModel


@dataclass(frozen=True)
class ProductFilters(BaseModel):
    search: str | None = None
