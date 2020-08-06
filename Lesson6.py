#Ex. 1
#Создать класс TrafficLight (светофор) и опредеor (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self._colour = (('red', 5), ('yellow', 2), ('green', 30))

    def running(self):
        for colour, sec in cycle(self._colour):
            print(colour)
            sleep(sec)

my_TrafficLight = TrafficLight()
my_TrafficLight.running()

#Ex. 2
#Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_weight(self):
        print('Asphalt weight needed: %i' % (int(self._length * self._width * 25 * 5 / 1000)))

my_road = Road(5000, 20)
my_road.asphalt_weight()

#Ex. 3
#Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным
# и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income_wage + self._income_bonus)

worker_1 = Position('Sergey', 'Semenov', 'specialist', {'wage': 50000, 'bonus': 5000})
worker_1.get_full_name()
worker_1.get_total_income()

#Ex. 4
#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула
# (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction):
        print('Машина повернула {}'.format(direction))

    def show_speed(self):
        print('Текущая скорость: ', self.speed)


class TownCar(Car):
    def show_speed(self):
        print('Текущая скорость:', self.speed)
        if self.speed > 60:
            print('Превышение скорости!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print('CТекущая скорость:', self.speed)
        if self.speed > 40:
            print('Превышение скорости!')

class PoliceCar(Car):
    pass

sport_car = SportCar(200, 'Красный', 'Молния', False)
town_car = TownCar(90, 'Белый', 'Ауди', False)
work_car = WorkCar(39, 'Черный', 'Мерседес', False)
police_car = PoliceCar(120, 'Синий', 'BMW', True)

sport_car.go()
town_car.stop()
work_car.turn("налево")

town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.show_speed()


#Ex. 5
#Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки. Инструмент - ручка.')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки. Инструмент - карандаш.')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки. Инструмент - маркер.')

pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()