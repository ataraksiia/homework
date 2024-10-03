class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list
    count_categories = 0
    count_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        Category.count_categories += 1
        Category.count_products += len(products)


# if __name__ == "__main__":
#     product1 = Product("iPhone 13", "128GB", 59_799.0, 100)
#     product2 = Product("iPhone 5", "32GB", 10_000.0, 1)
#     product3 = Product('55\" QLED 4K',"Фоновая подсветка", 123_000.0, 7)
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     print(product1.quantity)
#
#     print(product2.name)
#     print(product2.description)
#     print(product2.price)
#     print(product2.quantity)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство коммуникации и получение дополнительных функций для удобства жизни",
#         [product1, product2],
#     )
#     category2 = Category(
#         "Телевизоры",
#         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
#         [product3],
#     )
#
#     print(category1.name)
#     print(category1.description)
#     print(category1.products)
#
#     print(category2.name)
#     print(category2.description)
#     print(category2.products)
#
#     print(Category.count_categories)
#     print(Category.count_products)
