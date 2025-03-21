#4

'''
Создайте класс АВТОМОБИЛЬ с методами, 
позволяющими вывести на экран информацию об автомобиле, 
а также определить, подходит ли данный автомобиль для заданных условий. 
Создайте дочерние классы ЛЕГКОВОЙ АВТОМОБИЛЬ 
(марка, модель, год выпуска, тип кузова), ГРУЗОВОЙ АВТОМОБИЛЬ 
(марка, модель, год выпуска, грузоподъемность), АВТОБУС 
(марка, модель, год выпуска, количество мест) со своими методами 
вывода информации на экран и определения соответствия заданным условиям. 
Создайте список автомобилей, выведите полную информацию из базы на экран, 
а также организуйте поиск автомобилей с заданной маркой или годом выпуска.
'''

class Automobile:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")


class LightAutomobile(Automobile):
    def __init__(self, brand, model, year, body_type):
        super().__init__(brand, model, year)
        self.body_type = body_type

    def display_info(self):
        super().display_info()
        print(f"Тип кузова: {self.body_type}")


class Truck(Automobile):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def display_info(self):
        super().display_info()
        print(f"Грузоподъёмность: {self.load_capacity}")

class Bus(Automobile):
    def __init__(self, brand, model, year, num_seats):
        super().__init__(brand, model, year)
        self.num_seats = num_seats

    def display_info(self):
        super().display_info()
        print(f"Количество мест: {self.num_seats}")


automobiles = [
    LightAutomobile("Toyota", "Corolla", 2020, "Sedan"),
    Truck("Volvo", "FH16", 2022, 10),
    Bus("Mercedes", "Sprinter", 2018, 22),
    LightAutomobile("Ford", "Mustang", 2023, "Coupe"),
]

print("Все автомобили:")
for car in automobiles:
    car.display_info()
    print()

search_brand = "Toyota"
print(f"Поиск автомобиля с маркой: {search_brand}")
for car in automobiles:
    if car.brand == search_brand:
        car.display_info()
        print()

search_year = 2022
print(f"Поиск автомобиля года выпуска: {search_year}")
for car in automobiles:
    if car.year == search_year:
        car.display_info()
        print()