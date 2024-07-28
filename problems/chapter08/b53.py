import heapq
from collections import defaultdict

N, D = list(map(int, input().split()))
X, Y = [], []
for i in range(N):
    x, y = list(map(int, input().split()))
    X.append(x)
    Y.append(y)

reward_dict = defaultdict(list)
for i in range(N):
    x, y = X[i], Y[i]
    reward_dict[x].append(y)

reward = []
ans = 0
for d in range(1, D + 1):
    if len(reward_dict[d]) > 0:
        for val in reward_dict[d]:
            heapq.heappush(reward, -1 * val)
    
    if len(reward) > 0:
        ans += -1 * heapq.heappop(reward)
print(ans)
