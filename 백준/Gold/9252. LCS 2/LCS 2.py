import sys
input = sys.stdin.readline

# 이전 문제와는 다르게, LCS 의 길이 뿐만 아니라 LCS도 출력해야 한다.
str1 = input().rstrip()
str2 = input().rstrip()

length1 = len(str1)
length2 = len(str2)

# str1 을 고정하고 str2 순회하는 방식
matrix = [[0] * (length2 + 1) for _ in range(length1 + 1)]

for i in range(1, length1 + 1):
    for j in range(1, length2 + 1):
        if str1[i-1] == str2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

i, j = length1, length2
ans = []

# 역추적
# forward 시에 길이가 갱신될 때마다 그 문자만 append 하면,
# 같은 matrix[i][j] 값이 여러 경로(위, 왼, 대각선)로 만들어질 수도 있고,
# 그 매칭이 최종 LCS에 포함되는 매칭인 지는 모름
# 즉, DP 를 채우는 도중에는 아직 결론이 나지 않은 상태임

while i > 0 and j > 0:
    if str1[i-1] == str2[j-1]:
        ans.append(str1[i-1])
        i -= 1
        j -= 1
    else:
        if matrix[i-1][j] >= matrix[i][j-1]:
            i -= 1
        else:
            j -= 1

sys.stdout.write(str(matrix[length1][length2]) + '\n')

if matrix[length1][length2]:
    sys.stdout.write(''.join(reversed(ans)))