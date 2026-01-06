import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

matrix = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]

for i in range(1, len(str2)+1):
    for j in range(1, len(str1)+1):
        if str2[i-1] == str1[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

sys.stdout.write(str(max(map(max, matrix))))
