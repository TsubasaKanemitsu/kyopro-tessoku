N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

# 開始位置の決定
cnt = 0
right = 0
for i in range(N):
    while right < N and A[right] - A[i] <= K:
        right += 1
    cnt += right - (i + 1)
print(cnt)