N = int(input())
X, Y = [], []
for i in range(N):
    x, y = list(map(int, input().split()))
    X.append(x)
    Y.append(y)

Q = int(input())
A, B, C, D = [], [], [], []
for i in range(Q):
    a, b, c, d = list(map(int, input().split()))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

K = 1500
F = [[0] * (K + 1) for _ in range(K + 1)]
# 点のある位置
for i in range(N):
    F[X[i]][Y[i]] += 1

Z = [[0] * (K + 1) for _ in range(K + 1)]
# 行方向の累積和
for i in range(1, K + 1):
    for j in range(1, K + 1):
        Z[i][j] = Z[i][j - 1] + F[i][j]
# 列方向の累積和
for i in range(1, K + 1):
    for j in range(1, K + 1):
        Z[j][i] = Z[j - 1][i] + Z[j][i]
for i in range(Q):
    a, b, c, d = A[i], B[i], C[i], D[i]
    ans = (Z[c][d] + Z[a - 1][b - 1]) - (Z[c][b - 1] + Z[a - 1][d])
    print(ans)
    