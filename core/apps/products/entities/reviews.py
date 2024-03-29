from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime

from core.apps.common.enums import EntityStatus
from core.apps.customers.entities import Customer
from core.apps.products.entities.products import Product


@dataclass
class Review:
    id: int     # noqa
    product: Product | EntityStatus = field(EntityStatus.NOT_LOADED)
    customer: Customer | EntityStatus = field(EntityStatus.NOT_LOADED)
    text: str = field(default=" ")
    rating: int = field(default=1)
    created_at: datetime
