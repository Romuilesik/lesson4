while True:
    try:
        p = ""
        t = ""
        r = ""
        q1 = int(input('Введите число 1: '))
        q2 = int(input('Введите число 2: '))
        v = int(input('Какую операцию вы хотите выполнить?  1 Сложение  2 Вычитание  3 Деление  4 Умножение '))
        if v == 1:
            r = q1 + q2
            p = 'сложения'
            t = p
        elif v == 2:
            r = q1 - q2
            l = 'вычитания'
            t = l
        elif v == 3:
            r = float(q1 / q2)
            m = 'деления'
            t = m
        elif v == 4:
            r = q1 * q2
            n = 'умножения'
            t = n
        else:
            print("Выберите одно з действий")
            print('Результат ', t, ' = ', r)
        print('Результат ', t, ' = ', r)
    except ZeroDivisionError:
        print()
        print("На ноль делить нельзя")
    except ValueError:
            print("Это не число")