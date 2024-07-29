from typing import List
from collections import deque, defaultdict
N, M = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(M):
    a, b = list(map(int, input().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def bfs() -> List[int]:
    dist = [-1] * N
    queue = deque([0])
    dist[0] = 0
    while len(queue) > 0:
        pos = queue.pop()

        for next in graph[pos]:
            if dist[next] != -1:
                continue
            dist[next] = dist[pos] + 1
            queue.append(next)
    return dist

path = bfs()
for p in path:
    print(p)