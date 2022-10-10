def solution(survey, choices):
    answer = ''
    score = [0,0,0,0,0,0,0,0]
    category = ["R","T","C","F","J","M","A","N"]
    
    for i in range(len(survey)):
        point = 4-choices[i]
        num = category.index(survey[i][0])
        score[num] += point
        
    for i in range(4):
        if score[i*2] - score[i*2+1] >= 0:
            answer += category[i*2]
        else:
            answer += category[i*2+1]
        
    return answer
