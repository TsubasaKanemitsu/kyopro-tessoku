H, W, N = list(map(int, input().split()))
A, B, C, D = [], [], [], []
for i in range(N):
    a, b, c, d = list(map(int, input().split()))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

F = [[0] * (W + 2) for _ in range(H + 2)]
Z = [[0] * (W + 2) for _ in range(H + 2)]
for i in range(N):
    a, b, c, d = A[i], B[i], C[i], D[i]
    F[a][b] += 1
    F[c + 1][d + 1] += 1
    F[c + 1][b] -= 1
    F[a][d + 1] -= 1

# 行の累積和
for i in range(1, H + 1):
    for j in range(1, W + 1):
        Z[i][j] = Z[i][j - 1] + F[i][j]

# 列の累積和
for i in range(1, W + 1):
    for j in range(1, H + 1):
        Z[j][i] = Z[j - 1][i] + Z[j][i]

# 出力
for i in range(1, H+1):
	for j in range(1, W+1):
		if j >= 2:
			print(" ", end="")
		print(Z[i][j], end="")
	print("")