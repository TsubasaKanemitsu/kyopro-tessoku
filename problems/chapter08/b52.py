from collections import deque
N, X = list(map(int, input().split()))
X -= 1
A = list(input())

queue = deque([X])
A[X] = "@"
while len(queue) > 0:
    pos = queue.popleft()
    if pos - 1 >= 0 and A[pos - 1] == ".":
        A[pos - 1] = "@"
        queue.append(pos - 1)
    if pos + 1 <= N - 1 and A[pos + 1] == ".":
        A[pos + 1] = "@"    
        queue.append(pos + 1)
print(''.join(A))