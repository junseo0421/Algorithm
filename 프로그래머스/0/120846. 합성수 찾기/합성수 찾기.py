def is_prime_n(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
        
def solution(n):
    return len([i for i in range(2, n+1) if not is_prime_n(i)])