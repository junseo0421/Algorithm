import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())
liquid = list(map(int, input().split()))

min_diff = 1e12
min_lst = []

def search(start, end):
    global min_diff
    global min_lst

    if start >= end:
        return

    diff = liquid[start] + liquid[end]

    if abs(diff) < min_diff:
        min_diff = abs(diff)
        min_lst = (liquid[start], liquid[end])

    if diff == 0:
        return
    elif diff < 0:
        search(start+1, end)
    else:
        search(start, end-1)

search(0, N-1)

sys.stdout.write(" ".join(map(str, min_lst)))