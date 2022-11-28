# Задайте список из n чисел последовательности (1+1/n)^n   
# и выведите на экран их сумму.

list = []
n = int(input('Введите число:'))
sumnum = 0
for i in range(1, n + 1):
    sumnum = ((1+1/i)** i)
    list.append(sumnum)    
print(list)
res = map(float, list)
print(f'Сумма чисел: {sum(res)}')    
