n = int(input())
arr = list(map(int, input().split()))

MAX = 10**6
freq = [0] * (MAX + 1)

# count frequencies
for x in arr:
    freq[x] += 1

# print only numbers that appear
for i in range(1, MAX + 1):
    if freq[i] > 0:
        print(f"{i} -> {freq[i]}")
