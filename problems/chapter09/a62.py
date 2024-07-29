import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)
from collections import defaultdict

N, M = list(map(int, input().split()))
graph = defaultdict(list)

for i in range(M):
    a, b = list(map(int, input().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

arrived = [False] * N

# 現在地
pos = 0

def dfs(pos: int):
    arrived[pos] = True
    for next in graph[pos]:
        if not arrived[next]:
            dfs(next)

dfs(pos)
for i in range(N):
    if not arrived[i]:
        print("The graph is not connected.")
        exit()
print("The graph is connected.")
