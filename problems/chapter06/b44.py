N = int(input())
A = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    a = list(map(int, input().split()))
    for j in range(1, N + 1):
        A[i][j] = a[j - 1]
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

ROWS = [i for i in range(N + 1)]

for i in range(Q):
    typ, x, y = query[i]
    if typ == 1:
        temp = ROWS[x]
        ROWS[x] = ROWS[y]
        ROWS[y] = temp
    if typ == 2:
        print(A[ROWS[x]][y])