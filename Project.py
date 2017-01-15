#User Alexey Shmatok
#Group P3175


import math

def main():
    print('Операции:')
    print('1-Найти факториал числа')
    print('2-Найти корень квадратного уравнения')
    print('3-Найти определитель матрицы')
    N = input('Введите номер операции: ')
    if N == '1':
        print('A!')
        function1()
    elif N == '2':
        print('Ax^2+Bx+C=0')
        function2()
    elif N == '3':
        print('|a11, a12, a13|')
        print('|a21, a22, a23|')
        print('|a31, a32, a33|')
        function3()
    else:
        print('Введено неправильное значение')
        main()

def function1():
    A = float(input('Введите целочисленную операнду: '))
    B = int(A//1)
    if A-B == 0:
        if A >= 0:
            print('Факториал числа ', B, ' = ', math.factorial(B))
            main()
        else:
            print('Введено неправильное значение операнды')
            main()
    else:
        print('Введено неправильное значение операнды')
        main()

def function2():
    A = float(input('Введите первый коэффициент: '))
    B = float(input('Введите второй коэффициент: '))
    C = float(input('Введите третий коэффициент: '))
    D = float(B*B-4*A*C)
    if D < 0:
        print('Действительных решений не найдено')
        print('D = ', D)
        main()
    else:
        D = float(math.sqrt(D))
        X1 = (-B - D) / (2 * A)
        X2 = (-B + D) / (2 * A)
        print('Корни квадратного уравнения: ', X1, ' и ', X2)
        main()

def function3():
    a11 = float(input('Введите a11: '))
    a12 = float(input('Введите a12: '))
    a13 = float(input('Введите a13: '))
    a21 = float(input('Введите a21: '))
    a22 = float(input('Введите a22: '))
    a23 = float(input('Введите a23: '))
    a31 = float(input('Введите a31: '))
    a32 = float(input('Введите a32: '))
    a33 = float(input('Введите a33: '))
    Det = float(a11*a22*a33+a21*a32*a13+a12*a23*a31-a31*a22*a13-a21*a12*a33-a11*a32*a23)
    print('Определитель заданной матрицы = ', Det)
    main()

main()
