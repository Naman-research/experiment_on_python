from collections import Counter
n=int(input())
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
counter=Counter(a)
print(counter)