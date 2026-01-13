import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())  # 사람의 수, 파티의 수

tr_person = list(map(int, input().split()))  # 1부터 N까지

if tr_person[0] == 0:
    sys.stdout.write(str(M))
    exit()

# 1. 진실을 아는 사람 앞에서는 과장된 이야기를 하지 못 한다.
# 2. 진실을 아는 사람과 같은 파티에 있는 사람들에게도 과장된 이야기 못 함.

# 진실 못 말하는 집합 만들기?
# bfs로 풀어보기
# 이분 그래프를 이용 : 정점을 두 그룹으로 나눌 수 있고, 간선이 항상 서로 다른 그룹 사이에만 연결되는 그래프
# index 잘 생각해야할 듯 파티 번호도 1~M으로 indexing해서 맞추기?

party_members = [[] for _ in range(M+1)]  # 파티에 따른 멤버들 lst ex) party_members[1] = [1, 3, 4]  # 1번째 파티에는 1, 3, 4번째 사람이 속해있음
person_parties = [[] for _ in range(N+1)]  # 사람에 따른 파티 lst ex) person_parties[1] = [0] 1번째 사람은 0번째 파티에 속해있음

visited_pm = [0] * (M+1)  # 파티 중복 방문 방지
visited_pp = [0] * (N+1)  # 사람 중복 방문 방지

for i in range(1, M+1):  # 1~M 으로 party_members indexing
    members = list(map(int, input().split()))[1:]

    party_members[i] = members

    for m in members:  # 1부터 N까지
        person_parties[m].append(i)

q = deque()

for t in tr_person[1:]:
    q.append((0, t))  # 진실을 아는 사람의 번호 deque에 넣기

# type 0 : 사람 / type 1 : 파티

while q:
    type, num = q.popleft()

    if type == 0 and visited_pp[num] == 0:  # 사람, 1부터 N까지, 방문한 적이 없을 시
        visited_pp[num] = 1

        for pp in person_parties[num]:  # 해당 사람에 따른 파티 index lst
            q.append((1, pp))

    if type == 1 and visited_pm[num] == 0:
        visited_pm[num] = 1

        for pm in party_members[num]:  # 해당 파티에 따른 사람들 lst
            q.append((0, pm))

sys.stdout.write(str(M - sum(visited_pm)))
