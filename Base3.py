#Задача 3.
#Обсислити середнє арифметичне всіх додатних чисел у двовимірному масиві.
n=input("Введите масив через пробел")
n=n.split(' ')
sum=0
kol=0
for i in n:
    if i.isdigit():
        i=int(i)
        if i>0:
            sum=sum+i
            kol=kol+1
        else:
            print(i)
            print("Отрицательное")
    else:
        print(i)
        print("Не число")
print(sum/kol)