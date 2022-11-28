# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

number = float(input('Введите число:'))
str_number = str(number)
str_number = str_number.replace('.', '')
list_number = list(str_number)
lst_num = map(int, list_number)
result = sum(lst_num)
print(result)
