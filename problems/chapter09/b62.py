import sys
# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

from typing import Dict, List, Optional
from collections import defaultdict

N, M = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(M):
    a, b = list(map(int, input().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

arrived = [False] * N
stack = []
ans = []

def dfs(pos: int, graph: Dict[int, List[int]]) -> None:
    stack.append(pos)
    if pos == N - 1:
        print(*map(lambda x:x + 1, stack))
        exit()
    arrived[pos] = True

    for next in graph[pos]:
        if not arrived[next]:
            dfs(pos=next, graph=graph)
    stack.pop()

    return

dfs(pos=0, graph=graph)