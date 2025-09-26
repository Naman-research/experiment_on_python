n=int(input("Enter the length of array: "))
arr=[int(input()) for _ in range(n)]
max_sum=arr[0]
curr_sum=arr[0]
for i in range(1,n):
    # I want for each element it knows whether it is better it is beneficial to start anew or 
    # extend the previous max
    curr_sum=max(arr[i],curr_sum+arr[i])
    max_sum=max(max_sum,curr_sum)
print(max_sum)