T = int(input())
N = int(input())
L, R = [], []
for i in range(N):
    l, r = list(map(int, input().split()))
    L.append(l)
    R.append(r)

F = [0] * (T + 1)
for i in range(N):
    l, r = L[i], R[i]
    F[l] += 1
    F[r] -= 1

S = [0] * (T + 1)
S[0] = F[0]
for i in range(1, T + 1):
    S[i] = S[i - 1] + F[i]

for i in range(T):
    print(S[i])