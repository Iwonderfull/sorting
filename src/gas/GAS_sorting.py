import random

print("Fill at yourself 1, fill ar random 2")
inp = input("")
test = []
if inp == "1":
    test = list(map(int, input("Input integers separated via ',': ").split(",")))
else:
    print("Enter the size of array")
    n = int(input())
    for i in range(n):
        test.append(random.randint(1, 100))

print("Given:", test)


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(1, i):
            if array[j] > array[i]:
                array[j], array[i] = array[i], array[j]


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_arr = array[:mid]
        right_arr = array[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i, k, j = 0, 0, 0
        while i < len(left_arr) and k < len(right_arr):
            if left_arr[i] < right_arr[k]:
                array[j] = left_arr[i]
                i += 1
            else:
                array[j] = right_arr[k]
                k += 1
            j += 1

        while i < len(left_arr):
            array[j] = left_arr[i]
            j += 1
            i += 1

        while k < len(right_arr):
            array[j] = right_arr[k]
            j += 1
            k += 1


def choice_sort(array):
    for i in range(len(array)):
        temp_max = i
        for j in range(i, len(array)):
            if array[temp_max] > array[j]:
                temp_max = j
        array[i], array[temp_max] = array[temp_max], array[i]


def insert_sort(array):
    for i in range(len(array)):
        temp_i = i
        while temp_i > 0 and array[temp_i - 1] > array[temp_i]:
            array[temp_i], array[temp_i - 1] = array[temp_i - 1], array[temp_i]
            temp_i -= 1


def start_quick_sort(array):
    array = quick_sort(array, 0, len(array) - 1)
    print(*array)


def quick_sort(arr, s, e):
    if s < e:
        mid = (s + e) // 2
        pivot = arr[mid]
        index = partition(arr, s, e, pivot)
        quick_sort(arr, s, index - 1)
        quick_sort(arr, index, e)

    return arr


def partition(arr, k, r, pivot):
    while k <= r:
        while arr[k] < pivot:
            k += 1

        while arr[r] > pivot:
            r -= 1

        if k <= r:
            arr[k], arr[r] = arr[r], arr[k]
            k += 1
            r -= 1

    return k


def heap_sort(array):

    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

def heapify(array, n, i):

    largest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


sort_methods = {
    "bubble": bubble_sort,
    "insert": insert_sort,
    "choice": choice_sort,
    "quick": start_quick_sort,
    "merge": merge_sort,
    "heap": heap_sort,
}

method = input("Choose sort method: bubble, insert, choice, quick, merge, heap: ")
try:
    sort_func = sort_methods[method]
except KeyError as e:
    print(f"Unexpected sort method: {method}.")
    exit()
sort_func(test)
print(method)
print("Sorted:", test)
input("Press any key to exit...")
