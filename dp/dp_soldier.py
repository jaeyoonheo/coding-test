n = int(input())
soldier = list(map(int, input().split()))

soldier.revers()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if soldier[j] < soldier[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
