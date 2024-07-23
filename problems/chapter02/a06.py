N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
L = []
R = []
for i in range(Q):
    l, r = list(map(int, input().split()))
    L.append(l)
    R.append(r)

S = [0] * (N + 1)
S[0] = 0
for i in range(N):
    S[i + 1] = S[i] + A[i]

for i in range(Q):
    print(S[R[i]] - S[L[i] - 1])