from collections import defaultdict

def solution(tickets):
    answer = []
    
    path = defaultdict(list)
    for ticket in tickets:
        path[ticket[0]].append(ticket[1])
        
    for key in path.keys():
        path[key].sort()
    
    stack = ['ICN']
    
    while stack:
        top = stack[-1]
        if not path[top]:
            answer.append(stack.pop())
        else:
            stack.append(path[top].pop(0))
    answer.reverse()
    
    
    
    return answer
