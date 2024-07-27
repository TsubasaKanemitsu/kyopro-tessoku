N = int(input())
A, B = [], []
for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

res_plus_plus_A = []
res_plus_plus_B = []

res_plus_minus_A = []
res_plus_minus_B = []

res_minus_plus_A = []
res_minus_plus_B = []

res_minus_minus_A = []
res_minus_minus_B = []

for i in range(N):
    plus_plus = A[i] + B[i]
    if plus_plus >= 1:
        res_plus_plus_A.append(A[i])
        res_plus_plus_B.append(B[i])

    plus_minus = A[i] + -1 * B[i]
    if plus_minus >= 1:
        res_plus_minus_A.append(A[i])
        res_plus_minus_B.append(B[i])


    minus_plus = -1 * A[i] + B[i]
    if minus_plus >= 1:
        res_minus_plus_A.append(A[i])
        res_minus_plus_B.append(B[i])

    minus_minus = -1 * A[i] + -1 * B[i]
    if minus_minus >= 1:
        res_minus_minus_A.append(A[i])
        res_minus_minus_B.append(B[i])

pp = abs(sum(res_plus_plus_A) )+ abs(sum(res_plus_plus_B))
pm = abs(sum(res_plus_minus_A)) + abs(sum(res_plus_minus_B))
mp = abs(sum(res_minus_plus_A)) + abs(sum(res_minus_plus_B))
mm = abs(sum(res_minus_minus_A)) + abs(sum(res_minus_minus_B))
print(max(pp, pm, mp, mm))