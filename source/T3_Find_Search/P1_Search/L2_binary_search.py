def binary_search(array, x):
    """ Бінарний пошук у масиві

    :param array: Список елементів
    :param x: Шуканий елемент
    :return: True, якщо шуканий елемент знайдено
    """
    left = 0                # Індекс лівого елементу
    right = len(array) - 1  # Індекс правого елементу

    while left < right:
        m = left + (right - left) // 2  # Індекс середнього елементу
        if x > array[m]:
            left = m + 1
        else:
            right = m

    return array[right] == x


if __name__ == "__main__":
    a = [1, 2, 8, 13, 15, 17, 19, 20, 32, 42, 54, 92, 110, 222]
    print(binary_search(a, 17))
