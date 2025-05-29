def solution(i, j, k):
    count = 0
    for num in range(i, j+1):
        for i in str(num):
            if int(i) == k:
                count += 1
        
    return count