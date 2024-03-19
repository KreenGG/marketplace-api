from ninja import Router
from core.api.v1.products.handlers import router as products_router


router = Router()
router.add_router("/products", products_router)
