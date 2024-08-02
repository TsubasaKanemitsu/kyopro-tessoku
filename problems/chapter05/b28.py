N = int(input())
A = [0] * N
A[0] = 1
A[1] = 1

MOD = 10 ** 9 + 7
for i in range(2, N):
    a = A[i - 1] + A[i - 2]
    a %= MOD
    A[i] = a
print(A[N - 1])