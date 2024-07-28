N, Q = list(map(int, input().split()))

A = [ i for i in range(N + 1)]

query = []
for i in range (Q):
    q = list(input().split())
    query.append(q)

# 0: 反転なし, 1: 反転あり
order = 0
for i in range(Q):
    q = query[i]
    if q[0] == '1':
        x, y = int(q[1]), int(q[2])
        if order % 2 == 0:
            A[x] = y
        else:
            A[N - (x - 1)] = y
    if q[0] == '2':
        order += 1
    if q[0] == '3':
        x = int(q[1])
        if order % 2 == 0:
            print(A[x])
        else:
            print(A[N - (x - 1)])

