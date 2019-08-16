#Задача 4.
#У масиві [m][n] дійсних чисел знайти найменший елемент і вивести рядок
# у якому він знаходиться. Кількість рядків і ствопчиків вводить користувач.
n = int(input("Enter number rows :"))
m = int(input("Enter number cloums :"))
num_lst = []
i=0
for i in range(n):
    num_lst.append([int(j) for j in input("Enter a series of numbers across the space ").split()])
    print(len(num_lst[i]))

if len(num_lst[i])!=m:
    print("Количество столбиков вышло за предел")
i=i+1
nim_r=0
mm=num_lst[0][0]
n=0
for k in num_lst:
    for ii in k:
        if mm>ii:
            mm=ii
            nom_r=n
    n=n+1
print(mm)
print(num_lst[nom_r])