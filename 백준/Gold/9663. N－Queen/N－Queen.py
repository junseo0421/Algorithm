import sys
input = sys.stdin.readline

def main():
    N = int(input())
    count = 0

    cols = set()
    diag1 = set()
    diag2 = set()

    def backtracking(row):  # N 번
        nonlocal count

        if row == N:
            count += 1
            return

        for col in range(N):
            if not (col in cols or (row+col) in diag1 or (row-col) in diag2):
                cols.add(col); diag1.add(row+col); diag2.add(row-col)
                backtracking(row+1)
                cols.remove(col); diag1.remove(row+col); diag2.remove(row-col)

    backtracking(0)
    sys.stdout.write(str(count))

main()
