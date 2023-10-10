import math
print('Калькулятор')
f = int(input('Выберите функцию \n'
              'Сложение -- 1\n'
              'Вычитание -- 2\n'
              'Умножение -- 3\n'
              'Деление -- 4\n'
              'Возведение в квадрат -- 5\n'
              'Вычисление квадратного корня -- 6\n'
              'Вычисление синуса -- 7\n'
              'Вычисление косинуса -- 8\n'))
if f == 1:
    ch1 = int(input('Введите первое число: '))
    ch2 = int(input('Введите второе число: '))
    r = ch1 + ch2
elif (f == 2):
    ch1 = int(input('Введите первое число: '))
    ch2 = int(input('Введите второе число: '))
    r = ch1 - ch2
elif f == 3:
    ch1 = int(input('Введите первое число: '))
    ch2 = int(input('Введите второе число: '))
    r = ch1 * ch2
elif f == 4:
    ch1 = int(input('Введите первое число: '))
    ch2 = int(input('Введите второе число: '))
    r = float(ch1 / ch2)
elif (f == 5):
    ch = int(input('Введите число: '))
    r = ch * ch
elif (f == 6):
    ch = int(input('Введите число: '))
    sqrt = ch ** (0.5)
    r = sqrt
elif (f == 7):
    ch = int(input('Введите число: '))
    r = math.sin(ch)
elif (f == 8):
    ch = int(input('Введите число: '))
    r = math.cos(ch)
print('Ответ:', r)
