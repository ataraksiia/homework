# ООП

### В файле main.py пакета src

### Создан базовый абстрактный класс BaseProduct, который является родительским для класса продуктов

### Созданы классы: Product и Category

#### Product имеет свойства:
* название (name)
* описание (description)
* цена (price)
* количество в наличии (quantity)
#### _Update_ 06.10.24
* создан класс-метод new_product, который принимает на вход параметры товара в словаре и 
возвращает созданный объект класса Product; 
* атрибут цены сделан приватным, написаны геттеры и сеттеры цены;
* созданы магические методы __str__ и __add__;
В __add__ доработана функциональность сложения таким образом, чтобы можно было складывать товары только из одинаковых 
классов продуктов.
### Созданы наследники класса Product: Smartphone(Product) и LawnGrass(Product)
#### Smartphone(Product):
+ производительность (efficiency)
+ модель (model)
+ объем встроенной памяти (memory)
+ цвет (color)
#### LawnGrass(Product):
+ страна-производитель (country)
+ срок прорастания (germination_period)
+ цвет (color)

#### Создан класс-миксин MixinLog, который при инициализации объекта печатает в консоль информацию о том, 
#### от какого класса и с какими параметрами был создан объект.

#### Category имеет свойства:
* название (name)
* описание (description)
* список товаров категории (products)
* также добавлены два атрибута класса. Эти атрибуты хранят в себе количество категорий (category_count) 
  и количество товаров (product_count)
#### _Update_ 06.10.24
* cписок товаров теперь приватный. Для добавления товаров в категорию реализован метод add_product(), 
в который нужно передавать объект класса Product и уже его записывать в приватный атрибут списка товаров. 
Защищен метод так, чтобы, кроме смартфонов, газонной травы или других продуктов, в список
нельзя было добавлять ничего другого;
* реализован геттер products, который будет выводить список товаров в виде строк в формате:
"Название продукта, 80 руб. Остаток: 15 шт.";
* созданы магический метод __str__.

### В файле test_main.py пакета tests написаны тесты для main.py.