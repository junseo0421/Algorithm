import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

# 지수 법칙과 나머지 분배 법칙 이용

def multi(a, n):
    if n == 1:
        return a % c  # mod 값을 반환하며 재귀 종료
    else:
        tmp = multi(a, n // 2)
        if n % 2 == 0:  # tmp 는 이미 mod 값임
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

print(multi(a, b))
