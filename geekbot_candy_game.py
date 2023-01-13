n=2021
Flag=0
i=0
while n>0:
    if i==0:
        b=27
        n=n-b
        Flag=1
        i+=1
    else:
        b=29-a
        n=n-b
        Flag=1
    if n>0:
        while True:
            a=int(input('Игрок 2 введите число конфет от 1 до 28 включительно'))
            if a>28 or a<1:
                print('Вы ввели некорректное число, введите правильное число')
            else:    
                n=n-a
                Flag=2
                break
print(f'Победил игрок {Flag}') 

## игра с "умным" ботом, который все время выигрывает
