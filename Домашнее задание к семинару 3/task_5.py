#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#  - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('введите число: '))
fibo = []
f1, f2 = 1, 1
for i in range(n):
    fibo.append(f1)
    f1, f2 = f2, f1 + f2
l1, l2 = 0, 1
for i in range(n + 1):
    fibo.insert(0, l1)
    l1, l2 = l2, l1 - l2
print(fibo)
