import sys
input = sys.stdin.readline

def main():
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    team_list = []
    mn = 1e9

    def diff(team_list):
        score = 0
        for i in range(len(team_list)):
            for j in range(i+1, len(team_list)):
                a = team_list[i]
                b = team_list[j]
                score += matrix[a][b] + matrix[b][a]

        return score

    def dfs(start):
        nonlocal mn, team_list
        if len(team_list) == N//2:
            other_team_list = [i for i in range(N) if i not in team_list]
            s1 = diff(team_list)
            s2 = diff(other_team_list)
            s_diff = abs(s1 - s2)
            
            if s_diff < mn:
                mn = s_diff
            
            return

        for i in range(start, N):  # index 넘겨줌
            if not (i in team_list):
                team_list.append(i)
                dfs(i+1)
                team_list.pop()

    dfs(0)
    print(mn)

main()

