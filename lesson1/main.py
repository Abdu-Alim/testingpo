from lesson1 import add, substract, multiply, devide

print('Калькулятор')

a = float(input('Введите первое число: '))
operation = input('Введите операцию (+, -, *, /): ')
b = float(input('Введите второе число: '))

if operation == '+':
    result = add(a, b)
elif operation == '-':
    result = substract(a, b)
elif operation == '*':
    result = multiply(a, b)
elif operation == '/':
    result = devide(a, b)
else:
    result = 'Ошибка: неизвестная операция' 

print(f'Результат: {result}')