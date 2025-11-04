import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    ans = []

    def backtracking():
        if len(ans) == M:
            print(' '.join(map(str, ans)))
            return

        for num in range(1, N+1):
            if num not in ans:
                ans.append(num)
                backtracking()
                ans.pop()
            
    backtracking()

main()
