import sys

def min_moves_to_equal(nums):
    # Сначала найдем среднее значение списка
    average = sum(nums) // len(nums)

    # Посчитаем общее количество ходов для приближения каждого элемента к среднему значению
    total_moves = sum(abs(num - average) for num in nums)

    return total_moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Запустите программу из консоли, например так: python task4.py array.txt")
        sys.exit(1)
    file_name = sys.argv[1]

    # Чтение списка из файла
    with open(file_name, 'r') as file:
        nums = [int(line.strip()) for line in file]

    # Получение минимального количества ходов
    result = min_moves_to_equal(nums)
    print("Минимальное количество ходов:", result)
