import sys
input = sys.stdin.readline

N = int(input())
string = input().rstrip()
string_len = len(string)
string_alpha = [0] * 26

for s in string:
    string_alpha[ord(s) - 65] += 1

# 길이가 같을 때
# 완전히 같거나, 한 글자만 교체 가능해야 함

# 길이 차이가 1일 때
# 한 글자 추가 또는 삭제 가능해야 함

result = 0

for _ in range(N-1):
    nxt_s = input().rstrip()
    nxt_s_len = len(nxt_s)

    if abs(string_len - nxt_s_len) >= 2:
        continue

    judge = 0
    nxt_s_alpha = [0] * 26

    for s in nxt_s:
        nxt_s_alpha[ord(s) - 65] += 1

    for i in range(26):
        judge += abs(string_alpha[i] - nxt_s_alpha[i])

    if string_len == nxt_s_len and (judge == 0 or judge == 2):
        result += 1
    elif abs(string_len - nxt_s_len) == 1 and judge == 1:
        result += 1

print(result)
