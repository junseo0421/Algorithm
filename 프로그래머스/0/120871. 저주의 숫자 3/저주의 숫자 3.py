def solution(n):
    count = 0
    i = 0
    
    while i < n:  # n만큼 반복
        while (count + 1) % 3 == 0 or '3' in str(count + 1):
            count += 1
        count += 1
        i += 1

    return count