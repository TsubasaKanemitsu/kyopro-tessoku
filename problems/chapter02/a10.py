N = int(input())
A = list(map(int, input().split()))
D = int(input())
L, R = [0] * D, [0] * D
for i in range(D):
    l, r = list(map(int, input().split()))
    L[i], R[i] = l, r

LEFT = [0] * (N + 1)
LEFT[1] = A[0]
for i in range(1, N + 1):
    LEFT[i] = max(LEFT[i - 1], A[i - 1])

RIGHT = [0] * (N + 1)
RIGHT[N] = A[N - 1]
for i in range(1, N):
    RIGHT[N - i] = max(RIGHT[N - (i - 1)], A[N - (i + 1)])

for i in range(D):
    l, r = L[i], R[i]
    print(max(LEFT[l - 1], RIGHT[r + 1]))