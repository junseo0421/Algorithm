import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    ans = []
    visited = [False] * (N+1)
    
    def backtracking(start):
        if len(ans) == M:
            print(' '.join(map(str, ans)))
            return
        
        for i in range(start, N+1):
            if not visited[i]:
                visited[i] = True
                ans.append(i)
                backtracking(i+1)
                ans.pop()
                visited[i] = False
                
    backtracking(1)

main()
