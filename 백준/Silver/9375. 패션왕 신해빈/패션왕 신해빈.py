# 출처 : https://velog.io/@hamsangjin/%EB%B0%B1%EC%A4%80-9375%EB%B2%88-%ED%8C%A8%EC%85%98%EC%99%95-%EC%8B%A0%ED%95%B4%EB%B9%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    wears = {}
    cnt = 1

    for _ in range(N):
        name, type = input().split()

        if type not in wears:
            wears[type] = [name]
        else:
            wears[type].append(name)

    for n in wears.keys():
        cnt *= len(wears[n]) + 1

    print(cnt - 1)
