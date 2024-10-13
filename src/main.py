from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Базовый абстрактный класс BaseProduct, который является родительским для класса продуктов."""

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
        if self.quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
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

    def middle_price(self) -> Any:
        """Метод, который подсчитывает средний ценник всех товаров."""
        total_cost = 0
        quantity_products = 0
        for product in self.__products:
            quantity_products += product.quantity
            total_cost += product.price * product.quantity
        try:
            return total_cost / quantity_products
        except ZeroDivisionError:
            return 0


# if __name__ == '__main__':
#     try:
#         product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
#     except ValueError as e:
#         print(
#         "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
#     else:
#         print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")
#
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
#
#     print(category1.middle_price())
#
#     category_empty = Category("Пустая категория", "Категория без продуктов", [])
#     print(category_empty.middle_price())
