# 출처 : https://velog.io/@hamsangjin/%EB%B0%B1%EC%A4%80-5525%EB%B2%88-IOIOI-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

P = 'IOI'

cnt = i = answer = 0

while i < (M - 1):
  if S[i : i+3] == P:
    i += 2
    cnt += 1
    if cnt == N:
      answer += 1
      cnt -= 1

  else:
    i += 1
    cnt = 0

print(answer)