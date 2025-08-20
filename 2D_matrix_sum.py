''' 
Example 2D matrix of size 3×4 (3 rows, 4 columns):
[
  [1,  2,  3,  4],
  [5,  6,  7,  8],
  [9, 10, 11, 12]
]

1   2   3   4
5   6   7   8
9  10  11  12

'''
import sys
data=sys.stdin.buffer.read().split()
it=iter(data)
n=int(next(it))
m=int(next(it))
matrix=[]
a=data.pop(0)
b=data.pop(0) # New index 0 element 
for i in range(n):
    matrix.append(list(map(int,data[i*m:m+i*m])))
print(matrix)

q=sys.stdin.buffer.read().split()
it_1=iter(q)
n_1=int(next(it_1))
def resize(l,r):
    resized_matrix=[]
    sum_matrix=0
    for i in range(l):
        resized_matrix.append(sum(list(map(int,data[i*r:r+i*r]))))
        sum_matrix=sum(resized_matrix)
    return print(sum_matrix)
for i in range(n_1):
    l=int(next(it_1))
    r=int(next(it_1))
    resize(l,r)



        


    


