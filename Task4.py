# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) 
# -2 -1 0 1 2 Позиции: 0,1 -> 2

with open('file.txt','r') as f:    
    a = f.read().split('\n')
print(a)                              
list_elements = []                    
n = int(input('Введите число: '))           
for i in range (-n,n+1):                
    list_elements.append((i))         
print(list_elements)                                      
res = 1                                 
for item in a: 
    res *= list_elements[int(item)]
print(f' Произведение чисел равно: {res}')

