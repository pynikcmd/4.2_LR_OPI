#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Создать класс Fraction для работы с беззнаковыми дробными десятичными числами.
    Число должно быть представлено двумя списками типа int: целая и дробная часть,
    каждый элемент — десятичная цифра. Для целой части младшая цифра имеет
    меньший индекс, для дробной части старшая цифра имеет меньший индекс
    (десятые — в нулевом элементе, сотые — в первом, и т. д.). Реальный размер
    списоков задается как аргумент конструктора инициализации. Реализовать
    арифметические операции сложения, вычитания и умножения, и операции сравнения.
"""


class Fraction:
    def __init__(self, size):
        self.size = size
        self.integer_part = [0] * size  # Целая часть дроби
        self.fractional_part = [0] * size  # Дробная часть дроби
        self.count = 0  # Текущее количество элементов в списке

    def size(self):
        return self.size

    def __getitem__(self, index):
        # Перегрузка операции индексирования для доступа к элементам списка
        if 0 <= index < self.size:
            return (self.integer_part[::-1] + self.fractional_part)[index]
        else:
            raise IndexError("Индекс вне допустимого диапазона")

    def __setitem__(self, index, value):
        # Перегрузка операции присваивания для установки значения элемента списка
        if 0 <= index < self.size:
            if 0 <= value <= 9:
                if index < self.size // 2:
                    self.integer_part[self.size - 1 - index] = value
                else:
                    self.fractional_part[index - self.size // 2] = value
                self.count += 1
            else:
                raise ValueError("Значение должно быть от 0 до 9")
        else:
            raise IndexError("Индекс вне допустимого диапазона")

    def __str__(self):
        # Перегрузка операции преобразования объекта в строку для вывода
        integer_str = "".join(map(str, self.integer_part[::-1]))
        fractional_str = "".join(map(str, self.fractional_part))
        return f"{integer_str}.{fractional_str}"

    def __add__(self, other):
        if isinstance(other, Fraction):
            size = max(self.size, other.size)
            result = Fraction(size)
            carry = 0

            for i in range(size - 1, -1, -1):
                sum_ = self.__getitem__(i) + other.__getitem__(i) + carry
                carry = sum_ // 10
                result[i] = sum_ % 10

            if carry > 0:
                raise ValueError("Во время добавления произошло переполнение")

            return result
        else:
            raise ValueError("Неподдерживаемый тип операнда")

    def __sub__(self, other):
        # Перегрузка операции вычитания для объектов класса Fraction
        if isinstance(other, Fraction):
            size = max(self.size, other.size)
            result = Fraction(size)
            carry = 0

            for i in range(size - 1, -1, -1):
                diff = self[i] - other[i] - carry
                carry = 0
                if diff < 0:
                    carry = 1
                    diff += 10
                result[i] = diff

            if carry > 0:
                raise ValueError("При вычитании произошло недополнение")

            return result
        else:
            raise ValueError("Неподдерживаемый тип операнда")

    def __mul__(self, other):
        # Перегрузка операции умножения для объектов класса Fraction
        if isinstance(other, Fraction):
            size = self.size + other.size
            result = Fraction(size)

            for i in range(self.size - 1, -1, -1):
                carry = 0
                for j in range(other.size - 1, -1, -1):
                    prod = self[i] * other[j] + result[i + j + 1] + carry
                    carry = prod // 10
                    result[i + j + 1] = prod % 10

                result[i] = carry

            return result
        else:
            raise ValueError("Неподдерживаемый тип операнда")

    def __eq__(self, other):
        # Перегрузка операции равенства для объектов класса Fraction
        if isinstance(other, Fraction):
            return self.integer_part == other.integer_part and self.fractional_part == other.fractional_part
        else:
            raise ValueError("Неподдерживаемый тип операнда")

    def __ne__(self, other):
        # Перегрузка операции неравенства для объектов класса Fraction
        return not self == other

    def __lt__(self, other):
        # Перегрузка операции меньше для объектов класса Fraction
        if isinstance(other, Fraction):
            if self.integer_part < other.integer_part:
                return True
            elif self.integer_part == other.integer_part:
                return self.fractional_part < other.fractional_part
            else:
                return False
        else:
            raise ValueError("Неподдерживаемый тип операнда")

    def __le__(self, other):
        # Перегрузка операции меньше или равно для объектов класса Fraction
        return self < other or self == other

    def __gt__(self, other):
        # Перегрузка операции больше для объектов класса Fraction
        return not self <= other

    def __ge__(self, other):
        # Перегрузка операции больше или равно для объектов класса Fraction
        return not self < other


if __name__ == '__main__':
    # Создание объектов
    fraction1 = Fraction(5)
    fraction2 = Fraction(5)

    # Задание значений через индексирование
    fraction1[0] = 1
    fraction1[1] = 2
    fraction1[2] = 3
    fraction1[3] = 4
    fraction1[4] = 5

    fraction2[0] = 9
    fraction2[1] = 8
    fraction2[2] = 7
    fraction2[3] = 6
    fraction2[4] = 5

    # Печать значений
    print(fraction1)  # 5.4321
    print(fraction2)  # 5.6789

    # Примеры арифметических операций
    addition = fraction1 + fraction2
    print(addition)  # 11.1110

    subtraction = fraction1 - fraction2
    print(subtraction)  # -0.2468

    multiplication = fraction1 * fraction2
    print(multiplication)  # 28.86870

    # Примеры операций сравнения
    print(fraction1 == fraction2)  # False
    print(fraction1 != fraction2)  # True
    print(fraction1 < fraction2)  # True
    print(fraction1 <= fraction2)  # True
    print(fraction1 > fraction2)  # False
    print(fraction1 >= fraction2)  # False
