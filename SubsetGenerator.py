def SubsetGenerator(arr) -> None:
    result = []
    n = len(arr)
    for mask in range(1 << n):         # iterate over all 2^n masks
        subset = set()
        for j in range(n):
            if mask & (1 << j):
                subset.add(arr[j])
        result.append(subset)
    print(result)

print("Welcome to Subset Generator")
n = int(input("Please Enter The Length of the Subset-"))
arr = list(map(int, input().split()))
print(arr)
SubsetGenerator(arr)
