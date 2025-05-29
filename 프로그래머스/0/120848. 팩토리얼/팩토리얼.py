def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def solution(n):
    for i in range(11, 0, -1):
        if factorial(i) <= n:
            return i
