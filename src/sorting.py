from typing import List

test = list(map(int, input("Input integers separated via ',': ").split(",")))
print("Given:", test)


def bubble_sort(array: List, /):
    """Сортировка массива `array` методом пузырька"""
    N = len(array)
    # bypass - количество проходов.
    # Т.е. впервый раз пройдем до N-2'ого элемента и сравним его с N-1'ым.
    for bypass in range(1, N):
        for j in range(N - bypass):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def insert_sort(array: List, /):
    """Сортировка массива `array` методом вставки"""
    N = len(array)
    # top - элемент который будем вставлять.
    # И двигаясь справа налево начинаем искатье ему место.
    for top in range(1, N):
        k = top
        while k > 0 and array[k - 1] > array[k]:
            array[k], array[k - 1] = array[k - 1], array[k]
            k -= 1


def choice_sort(array: List, /):
    "Сортировка массива `array` методом выбора"
    N = len(array)
    # pos - вакантное место
    # Идём налево, начиная со следующего от pos элемента и выбираем кандидата
    for pos in range(N - 1):
        for k in range(pos + 1, N):
            if array[k] < array[pos]:
                array[k], array[pos] = array[pos], array[k]


sort_methods = {
    "bubble": bubble_sort,
    "insert": insert_sort,
    "choice": choice_sort,
}

method = input("Choose sort method: bubble, insert, choice: ")
try:
    sort_func = sort_methods[method]
except KeyError as e:
    print(f"Unexpected sort method: {method}.")
    exit()
print(sort_func.__doc__)
sort_func(test)
print("Sorted:", test)
