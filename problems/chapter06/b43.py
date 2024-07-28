N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

# 考察
# 全員がM問正解した状態で正解できなかった人が誰であるかをカウントして、Mから引けばいい

cnt = [M] * N
for i in range(M):
    cnt[A[i] - 1] -= 1

for i in range(N):
    print(cnt[i])