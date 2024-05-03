import sys
from collections import deque

if __name__ == "__main__":
    # Проверка количества переданных аргументов
    if len(sys.argv) != 3:
        print("Ошибка: неверное кол-во аргументов, пример:т python task1.py n m")
        sys.exit(1)
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    lst = ''.join(map(str, [i for i in range(1, n + 1)]))
    arr = deque(lst)
    res = list(arr[0])
    arr.rotate(-(m - 1))
    while arr[0] != lst[0]:
        res.append(arr[0])
        arr.rotate(-(m - 1))
    print(''.join(res))
