def solution(alp,cop,problems):
    answer = 0
    alp_target = 0
    cop_target = 0
    
    for problem in problems:
        alp_target = max(alp_target, problem[0])
        cop_target = max(cop_target, problem[1])
    
    dp = [[float('inf')]*(cop_target+1) for _ in range(alp_target+1)]
    dp[alp][cop] = 0
    
    for i in range(alp, alp_target+1):
        for j in range(cop, cop_target+1):
            if i < alp_target:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j < cop_target:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for alp_req, cop_req, alp_rwd, cop_rwd, time in problems:
                if i >= alp_req and j >= cop_req:                  
                    i_ = min(i+alp_rwd,alp_target)
                    j_ = min(j+cop_rwd,cop_target)
                    dp[i_][j_] = min(dp[i_][j_], dp[i][j] + time)
    
    return dp[alp_target][cop_target]
