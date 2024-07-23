N, K = list(map(int, input().split()))

cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        k = K - (i + j)
        if k >= 1 and k <= N:
            cnt += 1
print(cnt)