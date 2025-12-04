str_inp = input("Введите математическое действие: ") # действия: + - / * ^

ind_sign = 0
for i in range(len(str_inp)):
    if str_inp[i] in "+-*/^":
        ind_sign = i

sign = str_inp[ind_sign]
num_1 = float(str_inp[0:ind_sign])
num_2 = float(str_inp[(ind_sign + 1):len(str_inp)])

if sign == '+':
    res = num_1 + num_2
elif sign == '-':
    res = num_1 - num_2
elif sign == '*':
    res = num_1 * num_2
elif sign == '/':
    res = num_1 / num_2
else:
    res = num_1 ** num_2

print(f"{num_1} {sign} {num_2} = {res}", end='')
