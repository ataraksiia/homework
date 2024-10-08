from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Базовый абстрактный класс BaseProduct, который является родительским для класса продуктов."""

    name: str
    description: str
    # price: float
    quantity: int

    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any):
        pass


class MixinLog:
    """Класс-миксин, который при инициализации объекта печатает в консоль информацию о том,
    от какого класса и с какими параметрами был создан объект."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} ({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(MixinLog, BaseProduct):
    """Класс для продуктов."""

    name: str
    description: str
    # price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, dictionary: Any) -> Any:
        """Класс-метод, который принимает на вход параметры товара в словаре
        и возвращает созданный объект класса Product."""
        name = dictionary.get("name")
        description = dictionary.get("description")
        price = dictionary.get("price")
        quantity = dictionary.get("quantity")
        return cls(name, description, price, quantity)

    @property
    def price(self) -> Any:
        """Геттер для атрибута «цена»."""
        return self.__price

    @price.setter
    def price(self, price: Any) -> Any:
        """Сеттер для атрибута «цена»."""
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("Цена не должна быть нулевая или отрицательная")

    def __str__(self) -> str:
        """Строковое отображение продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other: Any) -> Any:
        """Сложение продуктов для получения полной стоимисти товаров на складе."""
        if type(self) is type(other):
            return self.quantity * self.__price + other.quantity * other.__price
        else:
            return TypeError


class Smartphone(Product):
    """Класс Smartphone - наследник класса Product."""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс LawnGrass - наследник класса Product."""

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Класс для категорий."""

    name: str
    description: str
    # products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Any) -> Any:
        """Метод, в который нужно передавать объект класса Product для записи продукта
        в приватный атрибут списка товаров."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только смартфоны, газонную траву или другие продукты.")

    @property
    def products(self) -> list:
        """Геттер, который выводит список товаров в виде строк в определенном формате."""
        products = []
        for product in self.__products:
            products.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
        return products

    def __str__(self) -> str:
        """Строковое отображение категории с общим числом всех продуктов."""
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
