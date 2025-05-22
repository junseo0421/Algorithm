def solution(n):
    answer = 0
    
    for x in range(0, n+1, 2):
        answer += x
        
    return answer