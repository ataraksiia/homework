from typing import Any

import pytest

from src.main import Category, Product


@pytest.fixture
def product1() -> Any:
    return Product(name="iPhone 13", description="128GB", price=59_799.0, quantity=100)


@pytest.fixture
def product2() -> Any:
    return Product(name="iPhone 5", description="32GB", price=10_000.0, quantity=1)


def test_product(product1: Any, product2: Any) -> Any:
    assert (
        product1.name == "iPhone 13"
        and product1.description == "128GB"
        and product1.price == 59_799.0
        and product1.quantity == 100
    )
    assert (
        product2.name == "iPhone 5"
        and product2.description == "32GB"
        and product2.price == 10_000.0
        and product2.quantity == 1
    )


@pytest.fixture
def category1(product1: Any, product2: Any) -> Any:
    return Category(
        name="Смартфоны", description="Смартфоны, как средство коммуникации", products=[product1, product2]
    )


def test_category(category1: Any, product1: Any, product2: Any) -> Any:
    assert (
        category1.name == "Смартфоны"
        and category1.description == "Смартфоны, как средство коммуникации"
        and category1.products == [product1, product2]
    )
