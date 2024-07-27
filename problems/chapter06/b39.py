from collections import defaultdict, deque

N, D = list(map(int, input().split()))
XY = []
for i in range(N):
    xy = list(map(int, input().split()))
    XY.append(xy)

for i in range(N):
    x, y = XY[i]

# タスク完了を管理する
finished = [False] * N
ans = 0
for i in range(D):
    # i日以降の中でまだ仕事をしていないかつ最大のお金がもらえる仕事を選ぶ
    max_value = 0
    max_id = -1
    for j in range(N):
        x, y = XY[j]
        x -= 1
        if finished[j]:
            continue
        if x <= i and y > max_value:
            max_id = j
            max_value = y
    if max_id != -1:
        finished[j] = True
        ans += XY[max_id][1]
print(ans)