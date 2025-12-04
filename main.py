def not_in(sign):
    return sign != '+' and sign != '-' and sign != '*' and sign != '/' and sign != '^'

# Блок ввода исходных данных
num_1 = int(input("Введите 1-ое целое число: "))
sign = input("Введите знак: ")
while not_in(sign):
    print("Оператор не поддерживается!")
    sign = input("Введите знак: ")
num_2 = int(input("Введите 2-ое целое число: "))
if sign == '/':
    while num_2 == 0:
        print("Деление на ноль не поддерживается!")
        num_2 = int(input("Введите 2-ое число отличное от нуля: "))

# Блок вычислений
if sign == '+':
    res = num_1 + num_2
elif sign == '-':
    res = num_1 - num_2
elif sign == '*':
    res = num_1 * num_2
elif sign == '/':
    res = num_1 // num_2
else:
    res = num_1 ** num_2

# Блок вывода результатов
print(f"{num_1} {sign} {num_2} = {res}", end='')
