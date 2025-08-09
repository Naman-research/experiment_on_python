'''
  *
 ***
***** for n=3

   *
  ***               
 *****
******* for n=5
'''
star="*"
n=int(input("Enter the lines of star needed:"))
for i in range(1,n+1):
    a=None
    print(((" ")*(n-i))+(star*(2*i-1)))