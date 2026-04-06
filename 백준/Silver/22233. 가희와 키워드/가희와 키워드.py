import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 메모장 키워드 수, 블로그 쓴 글 개수

q = set()

for _ in range(N):
    q.add(input().rstrip())

for _ in range(M):
    lst = list(input().rstrip().split(','))
    for k in lst:
        if k in q:
            q.remove(k)

    print(len(q))