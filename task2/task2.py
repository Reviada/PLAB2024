import math
import sys


# Функция для чтения центра окружности и её радиуса из файла
def read_circle(filename):
    with open(filename, 'r') as file:
        # Считываем координаты центра
        x, y = map(float, file.readline().split())
        # Считываем радиус
        radius = float(file.readline())
    return (x, y), radius


# Функция для чтения координат точек из файла
def read_points(filename):
    points = []
    with open(filename, 'r') as file:
        # Читаем каждую строку из файла
        for line in file:
            # Разделяем строку на координаты и добавляем точку в список
            x, y = map(float, line.split())
            points.append((x, y))
    return points


# Функция для вычисления расстояния между двумя точками
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


# Функция для определения положения точки относительно окружности
def point_position(center, radius, point):
    # Вычисляем расстояние от центра окружности до точки
    dist = distance(center, point)
    # Если расстояние равно радиусу, то точка лежит на окружности
    if dist == radius:
        return 0
    # Если расстояние меньше радиуса, то точка внутри окружности
    elif dist < radius:
        return 1
    # Иначе точка снаружи окружности
    else:
        return 2


# Основная функция программы
def main():
    # Проверяем количество переданных аргументов
    if len(sys.argv) != 3:
        print("Запустите программу из консоли, например так: python task2.py center.txt dots.txt")
        return None

    # Получаем имена файлов из аргументов командной строки
    center_file = sys.argv[1]
    dots_file = sys.argv[2]

    # Читаем центр окружности и радиус из файла
    center, radius = read_circle(center_file)
    # Читаем координаты точек из файла
    points = read_points(dots_file)

    # Для каждой точки определяем её положение относительно окружности и выводим результат
    for point in points:
        pos = point_position(center, radius, point)
        print(pos)


# Проверяем, запущена ли программа из консоли
if __name__ == "__main__":
    main()
