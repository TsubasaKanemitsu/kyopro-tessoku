N = int(input())
LR = []
for i in range(N):
    l, r = list(map(int, input().split()))
    LR.append([l, r])

# 考察
# 早く終わる順番にして、見れるものをどんどん見ていく？
LR.sort(key=lambda x:x[1])

start = 0
ans = 0
for i in range(N):
    l, r = LR[i]
    if start <= l:
        ans += 1
        start = r

print(ans)