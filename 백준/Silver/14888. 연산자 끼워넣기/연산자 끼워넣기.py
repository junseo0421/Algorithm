import sys
input = sys.stdin.readline

def main():
    N = int(input())
    num_list = list(map(int, input().split()))
    operations = list(map(int, input().split()))

    max_num = -1e9
    min_num = 1e9

    def dfs(n, temp):
        nonlocal max_num, min_num
        if n == N-1:
            max_num = max(temp, max_num)
            min_num = min(temp, min_num)
            return

        if operations[0] > 0:
            operations[0] -= 1
            dfs(n + 1, temp + num_list[n + 1])
            operations[0] += 1

        if operations[1] > 0:
            operations[1] -= 1
            dfs(n + 1, temp - num_list[n + 1])
            operations[1] += 1

        if operations[2] > 0:
            operations[2] -= 1
            dfs(n + 1, temp * num_list[n + 1])
            operations[2] += 1

        if operations[3] > 0:
            operations[3] -= 1
            dfs(n + 1, int(temp / num_list[n + 1]))
            operations[3] += 1

    dfs(0, num_list[0])

    print(max_num)
    print(min_num)

main()
