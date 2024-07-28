N, L = list(map(int, input().split()))
A, B = [], []
for i in range(N):
    a, b = list(input().split())
    A.append(int(a))
    B.append(b)

ans = 0
for i in range(N):
    if B[i] == 'E':
        ans = max(ans, L - A[i])
    else:
        ans = max(ans, A[i])
print(ans)