#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Поле first — дробное число, левая граница диапазона;
    поле second — дробное число, правая граница диапазона.
    Реализовать метод rangecheck() — проверку заданного числа
    на принадлежность диапазону.
"""


class Numb:
    def __init__(self, first, second):
        self.first = float(first)
        self.second = float(second)

    def __str__(self):
        return f"Pair: {self.first}, {self.second}"

    def __contains__(self, number):
        return self.first <= number <= self.second

    def read(self):
        self.first = float(input("Введите первое значение: "))
        self.second = float(input("Введите второе значение: "))

    def display(self):
        print(self)

    def rangecheck(self, number):
        if number in self:
            print(f"{number} находится в диапазоне.")
        else:
            print(f"{number} вне диапазона.")


def make_pair(first, second):
    return Numb(first, second)


if __name__ == '__main__':
    pair1 = Numb(1.5, 3.7)
    pair1.display()

    pair2 = make_pair(2.0, 4.5)
    pair2.display()

    number = float(input("Введите число для проверки диапазона: "))
    pair2.rangecheck(number)
