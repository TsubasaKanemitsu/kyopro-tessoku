from typing import List
from collections import deque

R, C = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))

M = [list(input()) for _ in range(R)]
def bfs(sx: int, sy:int) -> List[list]:
    dist = [[10 ** 5] * C for _ in range(R)]
    queue = deque([[sx, sy]])
    dist[sy][sx] = 0

    while len(queue) > 0:
        x, y = queue.pop()
        # 下、右、上、左
        pos = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for dy, dx in pos:
            X = x + dx
            Y = y + dy
            if not 0 <= X <= C - 1 or not 0 <= Y <= R - 1:
                continue
            if dist[Y][X] <= dist[y][x] + 1:
                continue 
            if M[Y][X] == "#":
                continue
            dist[Y][X] = dist[y][x] + 1
            queue.append([X, Y])

    return dist

dist = bfs(sx=sx-1, sy=sy-1)
print(dist[gy - 1][gx - 1])