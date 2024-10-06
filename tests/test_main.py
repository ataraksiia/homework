from typing import Any

import pytest

from src.main import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def product1() -> Any:
    return Product(name="iPhone 13", description="128GB", price=59_799.0, quantity=100)


@pytest.fixture
def product2() -> Any:
    return Product(name="iPhone 5", description="32GB", price=10_000.0, quantity=1)


@pytest.fixture
def smartphone1() -> Any:
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180_000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый",
    )


@pytest.fixture
def grass1() -> Any:
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )


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
    Category.category_count = 0
    Category.product_count = 0
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
    assert Category.category_count == 2 and Category.product_count == 2


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
    try:
        category1.add_product("Not a product")
    except TypeError:
        assert True


def test_products(category1: Any, product1: Any) -> None:
    assert category1.products == [
        "iPhone 13, 59799.0 руб. Остаток: 100 шт.\n",
        "iPhone 5, 10000.0 руб. Остаток: 1 шт.\n",
    ]


def test__str__product(product1: Any) -> None:
    """Тест вывода класса Product"""
    assert str(product1) == "iPhone 13, 59799.0 руб. Остаток: 100 шт.\n"


def test__add__(product1: Any, product2: Any, smartphone1: Any, grass1: Any) -> None:
    """Тест вывода класса Product"""
    assert product1 + product2 == 5989900.0 and smartphone1 + grass1 == TypeError


def test__str__category(category1: Any) -> None:
    """Тест вывода класса Category"""
    assert str(category1) == "Смартфоны, количество продуктов: 101 шт."


def test_smartphone(smartphone1: Any) -> None:
    """Тест класса Smartphone - наследника класса Product."""
    assert (
        smartphone1.name == "Samsung Galaxy S23 Ultra"
        and smartphone1.description == "256GB, Серый цвет, 200MP камера"
        and smartphone1.price == 180_000.0
        and smartphone1.quantity == 5
        and smartphone1.efficiency == 95.5
        and smartphone1.model == "S23 Ultra"
        and smartphone1.memory == 256
        and smartphone1.color == "Серый"
    )


def test_lawngrass(grass1: Any) -> None:
    """Тест класса LawnGrass - наследника класса Product."""
    assert (
        grass1.name == "Газонная трава"
        and grass1.description == "Элитная трава для газона"
        and grass1.price == 500.0
        and grass1.quantity == 20
        and grass1.country == "Россия"
        and grass1.germination_period == "7 дней"
        and grass1.color == "Зеленый"
    )
