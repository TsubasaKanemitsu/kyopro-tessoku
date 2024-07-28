from collections import deque

Q = int(input())
query = [list(input().split()) for _ in range(Q)]

q = deque()
for i in range(Q):
    qr = query[i]
    if qr[0] == "1":
        q.append(qr[1])
    if qr[0] == "2":
        print(q[0])
    if qr[0] == "3":
        q.popleft()
