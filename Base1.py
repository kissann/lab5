#Задача 1
#Створити алгоритм, за допомогою якого можна ввести дані у одновимірний числовий масив із консолі у однин рядок через пробіл.
flag=True
mas=[]
while flag:
    n=input("Введите ряд чисел через пробел ")
    arr=[]
    arr=n.split(' ')
    for i in arr:
        if i.isdigit():
            mas.append(i)
        elif i=='^':
            print('ВЫХОД')
            flag = False
            break
        else:
            print('Не число')
            flag=False
            break
    print(mas)

