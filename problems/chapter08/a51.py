from collections import deque
Q = int(input())
query = [list(input().split()) for _ in range(Q)]

stack = deque()
for i in range(Q):
    q = query[i]
    if q[0] == "1":
        stack.append(q[1])
    if q[0] == "2":
        print(stack[-1])
    if q[0] == "3":
        stack.pop()
