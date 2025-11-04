import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    ans = []

    def backtracking(start):
        if len(ans) == M:
            print(' '.join(map(str, ans)))
            return

        for i in range(start, N+1):
            ans.append(i)
            backtracking(i)
            ans.pop()

    backtracking(1)

main()
