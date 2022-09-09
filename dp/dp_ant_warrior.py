n = int(input())
storage = list(map(int, input().split()))
rst = [0] * (n)

for i in range(n):
    if i == 0:
        rst[i] = storage[i]
    elif i == 1:
        rst[i] = max(storage[i],storage[i-1])
    else:
        rst[i] = max(storage[i] + rst[i - 2],rst[i - 1])

print(rst[n - 1])
