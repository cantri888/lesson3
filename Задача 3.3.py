# Задача № 3: Реализовать функцию my_func(), которая принимает три позиционных аргумента и
#             возвращает сумму наибольших двух аргументов.
# Решение:

def my_func(a, b, c):
    print(f'Даны числа: {a}, {b}, {c}')

    list_num = [a, b, c]  # создаем список из принятых параметров

    # функция min вернет минимальный элемент в списке
    # а метод remove удаляем этот минимальный элемент
    list_num.remove(min(list_num))

    # возвращаем значение, которое вернет функция sum (сумма элементов списка)
    return sum(list_num)


# в переменной summa будет значение, которое вернулось из функции my_func
summa = my_func(9, 1, 8)

print(f'Сумма наибольших двух чисел из 3-ех = {summa}')
