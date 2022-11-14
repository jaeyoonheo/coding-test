def solution(alp, cop, problems):
    max_alp, max_cop = 0, 0
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])

    
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    dp = [[float('inf')]*(max_cop+1) for _ in range(max_alp+1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for alp_req, cop_req, alp_rwd, cop_rwd, time in problems:
                if i >= alp_req and j >= cop_req:                  
                    i_ = min(i+alp_rwd,max_alp)
                    j_ = min(j+cop_rwd,max_cop)
                    dp[i_][j_] = min(dp[i_][j_], dp[i][j] + time)

    return dp[-1][-1]
