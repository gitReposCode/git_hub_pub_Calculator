str_inp = input("Введите математическое действие: ")  # действия: + - / * ^

ind_sign = 0
for i in range(len(str_inp)):
    if str_inp[i] in "+-*/^":
        ind_sign = i

sign = str_inp[ind_sign]
num_1 = float(str_inp[:ind_sign])
num_2 = float(str_inp[(ind_sign + 1):])

match sign:
    case '+':
        res = num_1 + num_2
    case '-':
        res = num_1 - num_2
    case '*':
        res = num_1 * num_2
    case '/':
        res = num_1 / num_2
    case '^':
        res = num_1 ** num_2
    case '_':
        print("Данный оператор не поддерживается!")
        exit(0)

print(f"{num_1} {sign} {num_2} = {res}", end='')
