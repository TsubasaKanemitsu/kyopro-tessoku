N = int(input())
A, B, C, D = [], [], [], []
for i in range(N):
    a, b, c, d = list(map(int, input().split()))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

M = 1500
F = [[0] * (M + 1) for _ in range(M + 1)]
for i in range(N):
    a, b, c, d = A[i], B[i], C[i], D[i]
    F[a][b] += 1
    F[a][d] -= 1
    F[c][b] -= 1
    F[c][d] += 1

Z = [[0] * (M + 1) for _ in range(M + 1)]
# 初期化
for i in range(M + 1):
    Z[0][i] = F[0][i]
    Z[i][0] = F[i][0]

# 行の累積和
for i in range(0, M + 1):
    for j in range(1, M + 1):
        Z[i][j] = Z[i][j - 1] + F[i][j]
# 列の累積和
for j in range(0, M + 1):
    for i in range(1, M + 1):
        Z[i][j] = Z[i - 1][j] + Z[i][j]

area = 0
for i in range(M + 1):
    for j in range(M + 1):
        if Z[i][j] >= 1:
            area += 1
print(area)