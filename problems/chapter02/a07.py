D = int(input())
N = int(input())
L, R = [], []
for i in range(N):
    l, r = list(map(int, input().split()))
    L.append(l)
    R.append(r)

F = [0] * (D + 2)
for i in range(N):
    l, r = L[i], R[i]
    F[l] += 1
    F[r + 1] -= 1

S = [0] * (D + 2)
for i in range(D):
    S[i + 1] = S[i] + F[i + 1]

for i in range(1, D + 1):
    print(S[i])