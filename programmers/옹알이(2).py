def solution(babbling):
    answer = 0
    
    base = ["aya", "ye", "woo", "ma"]
    for x in babbling:
        stack = ''
        prev = ''
        
        for char in x:
            stack += char
            
            if prev != stack and stack in base:
                prev = stack
                stack = ''
                
        if len(stack) == 0:
            answer += 1
    
    return answer
