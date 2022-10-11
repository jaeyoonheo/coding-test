from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)

    des = (sum1 + sum2)
    if des%2 == 0:
        des = des//2
    else:
        return -1

    for i in range(len(queue1)*3):
        if sum1 == des:
            return i
        elif sum1 > des:
            sum1 -= queue1[0]
            queue2.append(queue1.popleft())
        else:
            sum1 += queue2[0]
            queue1.append(queue2.popleft())

    return -1
