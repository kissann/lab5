#Задача 5.
#Відсортувати кожен рядок двовимірного масиву у порядку зростання.
n = int(input("Enter number rows :"))
m = int(input("Enter number cloums :"))
num_lst = []
i=0
for i in range(n):
    num_lst.append([int(j) for j in input("Введите числа через пробел ").split()])
    print(len(num_lst[i]))

if len(num_lst[i])!=m:
    print("Количество столбиков вышло за предел")
for i in num_lst:
    i1=sorted(i)
    print(i1)