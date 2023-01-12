## сортировка выбором для python
from random import randint
alist=[]
for i in range(6):
    alist.append(randint(1,20))

print(alist)
n=len(alist)
for i in range(0,n-1):
    pos=i
    alist[i]
    for j in range(i+1,n):
        if alist[j]<alist[pos]:
           
            alist[j],alist[pos]=alist[pos],alist[j]
print(alist)
    
