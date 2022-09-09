n, m = map(int, input().split())
changes = [0] * n
dp = [10001] * (m + 1)
dp[0] = 0

for i in range(n):
    changes[i] = int(input())

for i in range(m + 1):
    for j in range(n):
      if dp[i-changes[j]] != 10001:
        dp[i] = min(dp[i], dp[i - changes[j]] + 1)

if dp[m] > 10000:
    print(-1)
else:
    print(dp[m])
