r"""
1. Test products count: product count zero, product count with existing products
2. Test product returns all, w\ paginagion, test filters (description, title, no match)
"""

import pytest

from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.services.products import BaseProductService
from tests.factories.products import ProductModelFactory


@pytest.mark.django_db
def test__get_products_count(product_service: BaseProductService):
    """Test product count zero with no products in database."""

    products_count = product_service.get_product_count(ProductFilters())
    assert products_count == 0, f"{products_count=}"


@pytest.mark.django_db
def test_get_products_count_exits(product_service: BaseProductService):
    """Test product count with existing products in database."""

    expected_count = 5
    ProductModelFactory.create_batch(size=expected_count)

    products_count = product_service.get_product_count(ProductFilters())
    assert products_count == expected_count, f"{products_count=}"


@pytest.mark.django_db
def test_get_products_zero(product_service: BaseProductService):
    """Test product empty list with no products in database."""

    fetched_products = product_service.get_product_list(ProductFilters(), PaginationIn())

    assert fetched_products == [], f"{fetched_products=}"


@pytest.mark.django_db
def test_get_products_all(product_service: BaseProductService):
    """Test product list with existing products in database."""

    expected_count = 5
    products = ProductModelFactory.create_batch(size=expected_count)
    products_titles = {product.title for product in products}

    fetched_products = product_service.get_product_list(ProductFilters(), PaginationIn())
    fetched_titles = {product.title for product in fetched_products}

    assert len(fetched_titles) == expected_count, f"{fetched_products=}"
    assert products_titles == fetched_titles, f"{fetched_titles=}"
