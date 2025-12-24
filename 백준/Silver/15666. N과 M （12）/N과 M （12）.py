import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

# 같은 depth 에서 동일 숫자 안 뽑기
# 해당 숫자 이후로부터 탐색

result = []

def back(start):
    prev = None
    if len(result) == M:
        sys.stdout.write(' '.join(map(str, result)) + '\n')
        return

    for i in range(start, N):  # lst index
        if prev != lst[i]:
            result.append(lst[i])
            prev = lst[i]
            back(i)
            result.pop()

back(0)