print("\t\t\tWelcome Martians")
print("\tIf you are reading this you are a native citizen of Mars")

n = int(input())
arr = list(map(int, input().split()))

permute = []
used = [False for _ in range(len(arr))]

def permutationGenerator(arr, n):
    if len(permute) == n:
        print(permute)
    else:
        for i in range(n):
            if not used[i]:
                permute.append(arr[i])
                used[i] = True
                permutationGenerator(arr, n)
                permute.pop()
                used[i] = False

permutationGenerator(arr, n)
