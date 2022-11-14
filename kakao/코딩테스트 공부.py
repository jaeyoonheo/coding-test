def solution(alp, cop, problems):
    answer = 0
    
    alp_target = max([i[0] for i in problems])
    cop_target = max([i[1] for i in problems])
    
    dp = [[0]*(cop_target+1) for _ in range(alp_target+1)]
    
    for i in range(alp_target+1):
        for j in range(cop_target+1):
            if i < 
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for problem in problems:
                if alp < problem[0]:
                    continue:
                if cop < pronlem[1]:
                    continue:
                
                dp[i+problem[2]][j+problem[3]] = min(dp[i+problem[2]][j+problem[3]], dp[i][j]+problem[4])
                
    answer = 
    
    return answer
