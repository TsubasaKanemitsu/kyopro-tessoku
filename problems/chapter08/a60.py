from collections import deque
N = int(input())
A = list(map(int, input().split()))

stack = deque()
ans = []
for i in range(N):
    if i >= 1:
        stack.append((i, A[i - 1]))
        while len(stack) > 0:
            if stack[-1][1] < A[i]:
                stack.pop()
            else:
                break
        
    if len(stack) == 0:
        ans.append(-1)
    else:
        ans.append(stack[-1][0])
print(*ans)