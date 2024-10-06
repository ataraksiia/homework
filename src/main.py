from typing import Any


class Product:
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


# if __name__ == '__main__':
#     smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
#                          "S23 Ultra", 256, "Серый")
#     smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
#     smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
#
#     print(smartphone1.name)
#     print(smartphone1.description)
#     print(smartphone1.price)
#     print(smartphone1.quantity)
#     print(smartphone1.efficiency)
#     print(smartphone1.model)
#     print(smartphone1.memory)
#     print(smartphone1.color)
#
#     print(smartphone2.name)
#     print(smartphone2.description)
#     print(smartphone2.price)
#     print(smartphone2.quantity)
#     print(smartphone2.efficiency)
#     print(smartphone2.model)
#     print(smartphone2.memory)
#     print(smartphone2.color)
#
#     print(smartphone3.name)
#     print(smartphone3.description)
#     print(smartphone3.price)
#     print(smartphone3.quantity)
#     print(smartphone3.efficiency)
#     print(smartphone3.model)
#     print(smartphone3.memory)
#     print(smartphone3.color)
#
#     grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
#     grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
#
#     print(grass1.name)
#     print(grass1.description)
#     print(grass1.price)
#     print(grass1.quantity)
#     print(grass1.country)
#     print(grass1.germination_period)
#     print(grass1.color)
#
#     print(grass2.name)
#     print(grass2.description)
#     print(grass2.price)
#     print(grass2.quantity)
#     print(grass2.country)
#     print(grass2.germination_period)
#     print(grass2.color)
#
#     smartphone_sum = smartphone1 + smartphone2
#     print(smartphone_sum)
#
#     grass_sum = grass1 + grass2
#     print(grass_sum)
#
#     try:
#         invalid_sum = smartphone1 + grass1
#     except TypeError:
#         print("Возникла ошибка TypeError при попытке сложения")
#     else:
#         print("Не возникла ошибка TypeError при попытке сложения")
#
#     category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
#     category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])
#
#     category_smartphones.add_product(smartphone3)
#
#     print(category_smartphones.products)
#
#     print(Category.product_count)
#
#     try:
#         category_smartphones.add_product("Not a product")
#     except TypeError:
#         print("Возникла ошибка TypeError при добавлении не продукта")
#     else:
#         print("Не возникла ошибка TypeError при добавлении не продукта")
