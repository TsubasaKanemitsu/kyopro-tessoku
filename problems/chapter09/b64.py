import heapq
from collections import defaultdict

N, M = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(M):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    graph[a].append([c, b])
    graph[b].append([c, a])


def bfs() -> list:
    Q = []
    visited = [False] * N
    dist = [-1] * N
    keiro = [-1] * N

    Q.append([0, 0])
    dist[0] = 0
    keiro[0] = 0

    while len(Q) > 0:
        # 距離、頂点
        _, v = heapq.heappop(Q)
        if visited[v]:
            continue
        visited[v] = True
        for cost, next in graph[v]:
            if dist[next] == -1 or dist[next] > dist[v] + cost:
                dist[next] = dist[v] + cost
                keiro[next] = v
                heapq.heappush(Q, (dist[next], next))
    return keiro, dist

keiro, dist = bfs()

cur = N - 1
ans = []
for i in range(N):
    ans.append(cur + 1)
    if cur == 0:
        break
    cur = keiro[cur]
    
print(*reversed(ans))