#Ex. 1
#1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, matrix_data):
        self.input = matrix_data

    def __str__(self):
        return '\n'.join([' '.join([str(ix) for ix in line]) for line in self.input])

    def __add__(self, other):
        result = ''
        for line_a, line_b in zip(self.input, other.input):
            result_line = [a + b for a, b in zip(line_a, line_b)]
            result = result + ' '.join([str(i) for i in result_line]) + '\n'

        return result

matrix_a = Matrix([[1, 2],[3, 4],])

matrix_b = Matrix([[5, 6],[7, 8],])

print(matrix_a)
print(matrix_b)
print(matrix_a.__add__(matrix_b))

#Ex. 2
#Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, parameter):
        self.parameter = parameter

    @abstractmethod
    def mat_consumption(self):
        pass

class Coat(Clothes):
    @property
    def mat_consumption(self):
        return(self.parameter / 6.5 + 0.5)

class Suit(Clothes):
    @property
    def mat_consumption(self):
        return(self.parameter * 2 + 0.3)

coat = Coat(54)
suit = Suit(180)

print(coat.mat_consumption)
print(suit.mat_consumption)
print(coat.mat_consumption + suit.mat_consumption)

#Ex. 3
#Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
# (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
# до целого числа.
#Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
# нуля, иначе выводить соответствующее сообщение.
#Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
# ячеек этих двух клеток.
#Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.
#В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
#Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

class Cell:
    def __init__(self, cell_num):
        self.cell_num = cell_num

    def make_order(self, num_in_row):
        return('\n'.join(['*' * num_in_row for _ in range (self.cell_num // num_in_row)]) + '\n' + '*' * (self.cell_num % num_in_row))

    def __str__(self):
        return self.cell_num

    def __add__(self, other):
        return str(self.cell_num + other.cell_num)

    def __sub__(self, other):
        if self.cell_num > other.cell_num:
            return self.cell_num - other.cell_num
        else:
            return 'Вычитание не возможно'

    def __mul__(self, other):
        return str(self.cell_num * other.cell_num)

    def __truediv__(self, other):
        return round(self.cell_num / other.cell_num)

cell_1 = Cell(15)
cell_2 = Cell(5)

print(cell_1.__add__(cell_2))
print(cell_1.__sub__(cell_2))
print(cell_2.__sub__(cell_1))
print(cell_1.__mul__(cell_2))
print(cell_1.__truediv__(cell_2))



