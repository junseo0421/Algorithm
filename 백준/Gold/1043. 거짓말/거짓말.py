import sys
input = sys.stdin.readline

N, M = map(int, input().split())
know_lst = list(map(int, input().split()))

if know_lst[0] == 0:
    print(M)
    exit()

know_lst = set(know_lst[1:])

party = []

for _ in range(M):
    party.append(set(list(map(int, input().split()))[1:]))

changed = True

while changed:
    changed = False
    for p in party:
        # 이 파티에 진실을 아는 사람이 적어도 한 명은 있는데, 파티 전체가 이미 다 알려진 상태는 아니다
        if p & know_lst and not p <= know_lst:  
            know_lst = know_lst | p
            changed = True

ans = 0

for p in party:
    if len(p & know_lst) == 0:
        ans += 1

print(ans)