# a(x+y)^2 + b(x-y) + cx = 0 парабола заданная четырьмя числами
from typing import NamedTuple


class Dot(NamedTuple):
    x: float
    y: float


class Line(NamedTuple):
    """ Прямая задана уравнением ax+by+c=0"""
    a: float
    b: float
    c: float


from tkinter import *

root = Tk()
canvasWidth = 800
canvasHeight = 500
can = Canvas(root, width=canvasWidth, height=canvasHeight, bg='white')
can.pack()

from math import sqrt


def canon(x, y):
    """ Заданная функция в каноническом виде. """
    return 2 * p * x == y ** 2


def f(x, y):
    """ Заданная функция. """
    return a * (x + y) ** 2 + b * (x - y) + c * x


def f_x(x):
    """ Заданная функция, выраженная через x.
    y = ..."""
    if (b ** 2 - 8 * a * b * x - 4 * a * c * x) < 0:
        return 1
    return (b - 2 * a * x + sqrt(b ** 2 - 8 * a * b * x - 4 * a * c * x)) / (2 * a) \
        if max else (b - 2 * a * x - sqrt(b ** 2 - 8 * a * b * x - 4 * a * c * x)) / (2 * a)


def f_y(y):
    """ Заданная функция, выраженная через y.
     x = ... """
    return -(b + c + 2 * a * y + sqrt(b ** 2 + 2 * b * c + c ** 2 + 8 * a * b * y + 4 * a * c * y)) / (2 * a)


def from_canon(dot: Dot):
    """ Преобразует точку из канонической системы координат в изначальную. """
    return Dot(dot.x * cos - dot.y * sin + x0, dot.x * sin + dot.y * cos + y0)


def to_canon(dot: Dot):
    """ Переводит точку из канонической системы координат в исходную. """
    return Dot(((dot.y - y0) - (dot.x - x0)) / sqrt(2),
               -((dot.y - y0) + (dot.x - x0)) / sqrt(2))


def count_distance_to_line(dot: Dot, line: Line):
    """ Считает расстояние от точки до прямой (длину перпендикуляра) """
    return abs(line.a * dot.x + line.b * dot.y + line.c) / sqrt(line.a ** 2 + line.b ** 2)


def count_distance(dot1, dot2):
    """ Считает расстояние между точками. """
    return sqrt((dot1.x - dot2.x) ** 2 + (dot1.y - dot2.y) ** 2)


def count_delta(dot: Dot):
    """ Считает отклонение от линии для точки. """
    return count_distance(dot, F) - count_distance_to_line(dot, dir)


def find_symm(dot: Dot):
    """ Находит симметричную точку относительно оси симметрии параболы. """
    t = (c ** 2 + 4 * b * c) / (sqrt(2) * a * 8 * (2 * b + c))
    return Dot(t - dot.y, t - dot.x)


# Если p<0, то парабола снизу
# Вершина это х0 и у0
def brez():
    if p > 0:
        x = -canvasWidth // 2
        y = round(f_x(x))
        delta = count_delta(Dot(x + 1, y - 1))
        # Отрисовка верхней половины ветви, идущей вниз
        while (x <= x0 or -1.14 < delta < 1.14) and y >= y0:
            if delta > 0:  # если точка С находится снаружи (C, D)
                d_delta = count_delta(Dot(x, y - 1))
                if delta < d_delta:  # C
                    x += 1
                y -= 1
            else:  # если точка С находится внутри (C, B)
                b_delta = count_delta(Dot(x + 1, y))
                if delta < b_delta:  # C
                    y -= 1
                x += 1
            delta = count_delta(Dot(x + 1, y - 1))
            draw_pixel(x, y)

        # Отрисовка впадинки отдельно, потому что x идет в обратном направлении
        delta = count_delta(Dot(x - 1, y - 1))
        while (y >= y0 or x <= x0) and -3.14 < delta < 3.14:
            if delta < 0:  # если точка С находится снаружи (C, D)
                d_delta = count_delta(Dot(x, y - 1))
                if delta > d_delta:  # C
                    x -= 1
                y -= 1
            else:  # если точка С находится внутри (C, B)
                b_delta = count_delta(Dot(x - 1, y))
                if delta > b_delta:  # C
                    y -= 1
                x -= 1
            delta = count_delta(Dot(x - 1, y - 1))
            draw_pixel(x, y)

    # Отрисовка в случае если ветвь находится снизу
    else:
        x = canvasWidth // 2
        y = round(f_x(x))
        delta = count_delta(Dot(x + 1, y - 1))
        # Отрисовка нижней половины ветви, идущей вверх
        while (x >= x0 or -1.14 < delta < 1.14) and y <= y0:
            if delta > 0:  # если точка С находится снаружи (C, D)
                d_delta = count_delta(Dot(x, y + 1))
                if delta < d_delta:  # C
                    x -= 1
                y += 1
            else:  # если точка С находится внутри (C, B)
                b_delta = count_delta(Dot(x - 1, y))
                if delta < b_delta:  # C
                    y += 1
                x -= 1

            delta = count_delta(Dot(x - 1, y + 1))
            draw_pixel(x, y)
        x -= 1

        # Отрисовка впадинки
        delta = count_delta(Dot(x - 1, y + 1))
        while (y <= y0 or x >= x0) and -3.14 < delta < 3.14:
            if delta < 0:  # если точка С находится снаружи (C, D)
                d_delta = count_delta(Dot(x, y + 1))
                if delta > d_delta:  # C
                    x += 1
                y += 1
            else:  # если точка С находится внутри (C, B)
                b_delta = count_delta(Dot(x + 1, y))
                if delta > b_delta:  # C
                    y += 1
                x += 1
            delta = count_delta(Dot(x + 1, y - 1))
            draw_pixel(x, y)


def draw_pixel(x, y):
    """ Отрисовка пикселя и симметричного ему. """
    can.create_rectangle((x + canvasWidth // 2, canvasHeight - y - canvasHeight // 2) * 2)
    s = find_symm(Dot(x, y))
    can.create_rectangle((s.x + canvasWidth // 2, canvasHeight - s.y - canvasHeight // 2) * 2)


a, b, c = [int(x) for x in input('Введите три числа: ').rsplit()]

if a == 0:
    print('Заданные параметры не подходят. Имеются комплексные решения. \n'
          'Фигура не может быть построена в данной системе координат.')
else:
    p = (2 * b + c) / (4 * sqrt(2) * a)
    x = canvasHeight // 2 if p < 0 else -canvasHeight // 2

    # Чтобы не перестраивать алгоритм в случае зеркальных параметров, их можно поменять на подходящие
    # так как график не изменится, но алгоритм можно не менять
    if p > 0 and (b - 2 * a * x + sqrt(b ** 2 - 8 * a * b * x - 4 * a * c * x)) / (2 * a) < (
            b - 2 * a * x - sqrt(b ** 2 - 8 * a * b * x - 4 * a * c * x)) / (2 * a) or \
            p < 0 and (b - 2 * a * x + sqrt(b ** 2 - 8 * a * b * x - 4 * a * c * x)) / (2 * a) > (
            b - 2 * a * x - sqrt(b ** 2 - 8 * a * b * x - 4 * a * c * x)) / (2 * a):
        a = -a
        b = -b
        c = -c
        p = (2 * b + c) / (4 * sqrt(2) * a)

    # Оси симметрии
    x0 = (-c ** 2 / (sqrt(2) * (16 * a * b + 8 * a * c)))
    y0 = (c / (4 * sqrt(2) * a))

    # Параметры угла поворота для канонического уравнения
    cos = -sqrt(2) / 2
    sin = sqrt(2) / 2

    # Директриса в изначальной системе координат
    dir = Line(cos, sin, p / 2 + x0 * cos + y0 * sin)

    # Координаты фокуса
    F = from_canon(Dot(p / 2, 0))

    # Отрисовка осей x и y
    can.create_line((canvasWidth // 2 + 1, 0), (canvasWidth // 2 + 1, canvasHeight), fill='red')
    can.create_line((0, canvasHeight // 2 + 1), (canvasWidth, canvasHeight // 2 + 1), fill='red')

    brez()
    print('Построено')
    root.mainloop()
