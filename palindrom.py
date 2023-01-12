// создать список которые одинаково читается с обе стороны

from random import randint
alist=[]
for i in range(5):
    a=randint(1,10)

    alist.append(a)
    alist.insert(0, a)
print(alist)      
