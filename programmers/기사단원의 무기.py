def solution(number, limit, power):
    answer = 0
    
    def getms(num):
        cnt = 0
        numrt = num**0.5
        for i in range(1,int(numrt)+1):
            if i*i == num:
                cnt += 1
            elif num % i == 0:
                cnt += 2
        return cnt
    
    for i in range(1,number+1):
        ms = getms(i)
        if ms > limit:
            answer += power
        else:
            answer += ms
        
    
    return answer
