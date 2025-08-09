'''
  *
 ***
*****
'''
star="*"
n=int(input("Enter the lines of star needed: "))
for i in range(1,n+1):
    print((star*(2*i-1)).center(2*n-1))