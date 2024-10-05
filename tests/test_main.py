from typing import Any

import pytest

from src.main import Category, Product


@pytest.fixture
def product1() -> Any:
    return Product(name="iPhone 13", description="128GB", price=59_799.0, quantity=100)


@pytest.fixture
def product2() -> Any:
    return Product(name="iPhone 5", description="32GB", price=10_000.0, quantity=1)


def test_product(product1: Any, product2: Any) -> None:
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


def test_category(category1: Any, product1: Any) -> None:
    assert category1.name == "Смартфоны" and category1.description == "Смартфоны, как средство коммуникации"


def test_count_categories_and_count_products() -> None:
    Category.count_categories = 0
    Category.count_products = 0
    _ = Category(
        "Смартфоны",
        "Смартфоны, как средство коммуникации и получение дополнительных функций для удобства жизни",
        ["product1", "product2"],
    )
    _ = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [],
    )
    assert Category.count_categories == 2 and Category.count_products == 2


def test_new_product(product2: Any) -> None:
    product_data = Product.new_product({"name": "iPhone 5", "description": "32GB", "price": 10000.0, "quantity": 1})
    assert (
        product_data.name == product2.name
        and product_data.description == product2.description
        and product_data.price == product2.price
        and product_data.quantity == product2.quantity
    )


def test_get_price(product1: Any) -> None:
    assert product1.price == 59799.0


def test_set_price(product1: Any) -> None:
    product1.price = 70_000
    assert product1.price == 70_000

    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product1.price = -1
    assert product1.price == 70_000


def test_add_products(category1: Any, product1: Any) -> None:
    category1.add_product(product1)
    assert category1.add_product(product1) is None


def test_products(category1: Any, product1: Any) -> None:
    assert category1.products == [
        "iPhone 13, 59799.0 руб. Остаток: 100 шт.\n",
        "iPhone 5, 10000.0 руб. Остаток: 1 шт.\n",
    ]
