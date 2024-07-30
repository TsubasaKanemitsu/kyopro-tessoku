import heapq
from typing import List
from collections import defaultdict
N, M = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(M):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    graph[a].append([c, b])
    graph[b].append([c, a])

def dijkstra() -> List[int]:
    
    Q = []
    Q.append([0, 0])
    
    dist = [-1] * N
    visited = [False] * N

    dist[0] = 0

    while len(Q) > 0:
        _, v = heapq.heappop(Q)

        if visited[v]:
            continue
        visited[v] = True

        for cost, next in graph[v]:
            if dist[next] == -1 or dist[next] > dist[v] + cost:
                dist[next] = dist[v] + cost
                heapq.heappush(Q, (dist[next], next))

    return dist

dist = dijkstra()
for d in dist:
    print(d)