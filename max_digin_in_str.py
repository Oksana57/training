// нахождение максимального количества числе подряд в строке

str1='ghj2345fgd2345566fgds23'
count=0
max=0
for i in str1:
    if i.isdigit():
        count+=1
        if max<count:
            max=count
    else:
        count=0
print(max) 
