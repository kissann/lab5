#Задача 1
#GC-склад є важливою характеристикою геномних послідовностей і визначається як процентне співвідношення суми всього гуаніна
# і цитозина до загальної кількості нуклеїнових кислот в геномної послідовності.
#Напишіть програму, яка обчислюється процентний вміст символів G (гуанін) і C (цитозин) у введеному рядку
# (програма не повинна залежати від регістру символів, що вводять).
#Наприклад, в рядку "acggtgttat" процентний вміст символів G і C рівно 4/10*100 = 40.0, де 4 - це
# кількість символів G і C, а 10 - це довжина рядка.
s=input("Введите строку")
s=list(s)
kol=0
for i in s:
    i=i.lower()
    if (i=='g' or i=='c'):
        kol=kol+1
dl=len(s)
proz=(kol/dl)*100
print(proz)

