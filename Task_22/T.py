#Задача 22:
#Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются
#в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
#элементов второго множества. Затем пользователь вводит сами элементы
#множеств.


n = int(input("Количество элементов первого множества (N):"))
m = int(input("Количество элементов второго множества (M):"))
array1 = []
array2 = []
import random
for i in range(n):
    x1 = int(input())
    array1.append(x1)
for i in range(m):
    x2 = int(input())
    array2.append(x2)
print(array1)
print(array2)
array = []
for x in set(array1+array2):
  t = min(array1.count(x), array2.count(x))
  if t > 0:
    array += [x] * t
print(array)

