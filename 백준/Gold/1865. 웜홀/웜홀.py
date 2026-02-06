import sys
input = sys.stdin.readline

TC = int(input())
INF = float('inf')

def bf(N, edges):
    # dist를 0으로 초기화한 것은 모든 정점을 시작점으로 둔 것과 같은 효과, 사이클 판정에만 안전함
    # 정확한 최단거리를 보장하는 게 아니라, 모든 component 를 커버하며 음수 사이클이 있으면 잡아내기 위함
    # dist 를 어떤 값으로 두든 음수 사이클이 존재하면 N번째에도 갱신이 일어남
    # 반대로 음수 사이클이 없으면, 아무리 시작값을 0으로 깔아도 결국 어느 시점부터 갱신이 되지 않음
    dist = [0] * (N+1)

    for i in range(1, N+1):
        updated = False

        for start_node, next_node, cost in edges:  # 모든 간선 확인
            if dist[next_node] > dist[start_node] + cost:
                dist[next_node] = dist[start_node] + cost
                updated = True

                if i == N:  # n 번째 사이클에서도 값이 갱신되면 음수 순환 존재
                    return True

        if not updated:  # 가지 치기, 더 이상 갱신 없으면 조기 종료
            return False

    return False


for _ in range(TC):
    N, M, W = map(int, input().split())

    edges = []

    for _ in range(M):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(W):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    sys.stdout.write("YES\n" if bf(N, edges) else "NO\n")
