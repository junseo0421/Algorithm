def factorial(i):
    fact = 1
    for i in range(2, i+1):
        fact *= i
    return fact

def solution(balls, share):
    return factorial(balls) / (factorial(balls-share) * factorial(share))