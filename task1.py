#1

'''
Создайте класс "Магазин" с атрибутами название и список товаров. 
Каждый товар представлен классом
Товар с атрибутами название, цена, количество. 
Напишите методы для добавления товара в магазин,
удаления товара из магазина и вычисления общей стоимости товара в магазине. 
Используйте магический
метод `__len__` для определения количества товаров в магазине.
'''

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (Цена: {self.price}, Кол-во: {self.quantity})"

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Товар '{product.name}' удален из магазина '{self.name}'.")
        else:
            print(f"Товара '{product.name}' нет в магазине '{self.name}'.")

    def calculate_total_cost(self):
        total_cost = 0
        for product in self.products:
            total_cost += product.price * product.quantity
        return total_cost

    def __len__(self):
        return len(self.products)

    def display_products(self):
        if not self.products:
            print(f"В магазине '{self.name}' нет товаров.")
        else:
            print(f"Товары в магазине '{self.name}':")
            for product in self.products:
                print(f"- {product}")

product1 = Product("Вода", 50, 10)
product2 = Product("Хлеб", 30, 5)
product3 = Product("Молоко", 80, 3)

magazine = Store("Продуктовый магазин")
magazine.add_product(product1)
magazine.add_product(product2)
magazine.add_product(product3)

magazine.display_products()

print(f"Всего товаров в магазине: {len(magazine)}")
print(f"Общая стоимость товаров в магазине: {magazine.calculate_total_cost()}")

magazine.remove_product(product2)
magazine.display_products()

print(f"Всего товаров в магазине: {len(magazine)}")
print(f"Общая стоимость товаров в магазине: {magazine.calculate_total_cost()}")


product4 = Product("Шоколад", 100, 2)
magazine.remove_product(product4)