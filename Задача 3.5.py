# Задача № 5: Программа запрашивает у пользователя строку чисел, разделённых пробелом.
#             При нажатии Enter должна выводиться сумма чисел.
#             Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
#             Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
#             Но если вместо числа вводится специальный символ, выполнение программы завершается.
#             Если специальный символ введён после нескольких чисел,
#             то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
# Решение:

# при создании функции, она принимает параметр список, в котором хранятся введеные числа
def calc_sum(list_n):
    # результат в виде суммы всех чисел в списке
    result = 0
    # переключатель, если False, то цикл while (из которого вызывали функцию) прекратится с помощью оператора break
    fl = True

    # идем по списку
    # i - элемент списка (начиная с 0 индекса)
    for i in list_n:
        # конструкция try except помогает помочь определить ввели ли специальный символ (=) или нет
        # если его не ввели, то в try высчитывается сумма всех элементов списка, при этом каждый элемент списка
        # преобразовывается в вещественное число (т.е. оно может быть с плавающей точкой т.е. дробным или целым)
        # но, если в списке будет =, то его преобразовать не выйдет т.к. невозможно преобразовать спец символ в цифру
        # и произойдет ошибка ValueError, которую перехватим, что бы изменить наш переключатель
        try:
            result += float(i)
        except ValueError:
            fl = False

    # возвращаем сумму введенных чисел и положение переключателя
    return result, fl


print('Вводите, пожалуйста, числа в одну строку, где разделитель между числами - ПРОБЕЛ')
print('Для прекращения ввода, введите символ: =')
print()

finish_sum = 0

while (True):
    # вводим числа с разделителем - ПРОБЕЛ
    # функция split возвращает список, где 0 элемент списка то, что было введено до символа ПРОБЕЛ
    list_num = input('Введите, пожалуйста числа: ').split()

    # вызов функции, которая возвращает 2 значения, которые в свою очередь записываются в переменные summa и flag
    summa, flag = calc_sum(list_num)

    # подсчет конечной суммы
    # согласно условию задачи, пользователь может вновь вводить числа и поэтому +=
    finish_sum += summa

    print(f'Сумма введеных чисел = {finish_sum}')

    # если после вызова функции переменная flag НЕ True:
    if (not flag):
        # прерываем цикл while, тем самым завершив работу программы
        break
