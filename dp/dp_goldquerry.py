t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    gq_flatten = list(map(int, input().split()))
    gq = []
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        gq.append(gq_flatten[i * m:i * m + m])

    for j in range(m):
        for i in range(n):
            if j == 0:
                dp[i][j] = gq[i][j]
            else:
                if i == 0:
                    dp[i][j] = gq[i][j] + max(dp[i][j - 1], dp[i + 1][j - 1])
                elif i == n - 1:
                    dp[i][j] = gq[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1])
                else:
                    dp[i][j] = gq[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1],
                                              dp[i + 1][j - 1])

    print(max([i[m - 1] for i in dp]))
