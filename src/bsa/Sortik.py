str = input("Введите через \",\" цифры для сортировки: ")
str_array = str.split()
str_array2 = str.split()
str_array3 = str.split()
len_ar = len(str_array)


def sortik_bubble(array):
    # Сортировка пузырьком
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    print('Сортировка Пузырьками:', *array)


def sortik_insert(array):
    if len(array) <= 1:
        return
    for i in range(1, len(array)):
        s = array[i]
        j = i - 1
        while j >= 0 and s < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = s
    print('Сортировка Вставкой:', *array)


def sortik_choice(array):
    # Сортировка выбором
    for i in range(len(array) - 1):
        s = i
        for j in range(i + 1, len(array)):
            if array[j] < array[s]:
                s = j
        array[i], array[s] = array[s], array[i]
    print('Сортировка Выборкой:', *array)


sortik_bubble(str_array)
sortik_insert(str_array2)
sortik_choice(str_array3)
