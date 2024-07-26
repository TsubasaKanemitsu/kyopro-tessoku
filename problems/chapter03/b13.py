N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

sum = 0
cnt = 0
# 開始位置
for i in range(N):
    sum = 0
    right = i
    # 右に進むにつれて加算する
    while right < N and sum + A[right] <= K:
        sum += A[right]
        right += 1
    cnt += right - i
    # 開始位置が右に1つずれるので、合計から現時点の開始位置の品物の金額を減らす
    sum -= A[i]
print(cnt)