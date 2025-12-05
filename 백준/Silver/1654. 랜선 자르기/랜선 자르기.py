import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lst = [int(input()) for _ in range(K)]

# 이분 탐색
# end = sum(lines) // N 를 사용할 수도 있겠지만, 0이 나올 경우도 고려해야해서 아래와 같이 간결하게 사용
start, end = 1, max(lst)

while start <= end:
    mid = (start + end) // 2

    cnt = 0

    for num in lst:
        cnt += num // mid

    if cnt >= N:  # N개의 랜선을 만들 수 있음
        start = mid + 1
    else:  # 만들 수 없음
        end = mid - 1  # 만들 수 없는 mid랑 오른쪽 부분을 모두 버림

sys.stdout.write(str(end))  # end에 최대로 가능한 길이가 들어있음. start = end + 1 (조건이 깨지는 첫 길이)
