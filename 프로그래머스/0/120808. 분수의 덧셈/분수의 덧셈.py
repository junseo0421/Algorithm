def solution(numer1, denom1, numer2, denom2):
    bm = denom1 * denom2
    bj = numer1 * denom2 + numer2 * denom1
    
    x = max(bm, bj)
    
    for i in range(x, 0, -1):
        if bm % i == 0 and bj % i == 0:
            y = i
            break
    
    answer = [bj / y, bm / y]
    
    return answer