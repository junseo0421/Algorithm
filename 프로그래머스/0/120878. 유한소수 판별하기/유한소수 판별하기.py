import math

def solution(a, b):
    x = math.gcd(a, b)
    b = b // x
    
    while b != 1:
        if b % 2 == 0:
            b = b // 2
        elif b % 5 == 0:
            b = b // 5
        else:
            return 2
    
    return 1