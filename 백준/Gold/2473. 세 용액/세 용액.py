import sys
input = sys.stdin.readline

# 산성 용액 : 양의 정수
# 알칼리 용액 : 음의 정수

# 합이 0에 가장 가까운 혼합 용액

N = int(input())
num_lst = sorted(list(map(int, input().split())))

# 세 용액의 특성값의 오름차순으로 출력

min_sum = float('inf')
min_lst = []

for i in range(N-2):
    left = i + 1
    right = N - 1

    while left != right:
        summation = num_lst[i] + num_lst[left] + num_lst[right]

        if abs(summation) < min_sum:
            min_sum = abs(summation)
            min_lst = [i, left, right]

        if summation < 0:
            left += 1
        elif summation > 0:
            right -= 1
        else:
            min_lst = [i, left, right]
            break

for n in sorted(min_lst):
    sys.stdout.write(str(num_lst[n]) + ' ')