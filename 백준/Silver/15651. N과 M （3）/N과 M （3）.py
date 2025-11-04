import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    ans = []

    def backtracking():
        if len(ans) == M:
            print(' '.join(map(str, ans)))
            return

        for i in range(1, N+1):
            ans.append(i)
            backtracking()
            ans.pop()
    
    backtracking()

main()
