from random import randint

n=201
Flag=0
while n>0:
    a=int(input('Игрок 1 введите число конфет от 1 до 28 включительно'))
    n=n-a
    Flag=1
    if n>0:
        b=randint(1,28)
        n=n-b
        Flag=2
print(f'Победил игрок {Flag}') 

//игра в конфеты с ботом
