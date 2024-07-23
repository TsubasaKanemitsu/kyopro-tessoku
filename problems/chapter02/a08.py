H, W = list(map(int, input().split()))
X = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(1, H + 1):
    xs = list(map(int, input().split()))
    for j in range(1, W + 1):
        X[i][j] = xs[j - 1]

Q = int(input())
A, B, C, D = [], [], [], []
for i in range(Q):
    a, b, c, d = list(map(int, input().split()))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

Z = [[0] * (W + 1) for _ in range(H + 1)]
# Zの行の初期化
for i in range(1, H + 1):
    Z[i][1] = X[i][1]
# Zの列の初期化
for i in range(1, W + 1):
    Z[1][i] = X[1][i]

# 行の累積和
for i in range(1, H + 1):
    for j in range(1, W + 1):
        Z[i][j] = Z[i][j - 1] + X[i][j]

# 列の累積和
for i in range(1, W + 1):
    for j in range(1, H + 1):
        Z[j][i] = Z[j - 1][i] + Z[j][i]

for i in range(Q):
    a, b, c, d = A[i], B[i], C[i], D[i]
    ans = (Z[c][d] + Z[a - 1][b - 1]) - (Z[c][b - 1] + Z[a - 1][d])
    print(ans)