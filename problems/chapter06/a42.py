N, K = list(map(int, input().split()))
A, B = [], []
max_val = 0
for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

ans = 0
for a in range(1, 101):
    for b in range(1, 101):
        cnt = 0
        for i in range(N):
            if a <= A[i] <= a + K and b <= B[i] <= b + K:
                cnt += 1
        ans = max(ans, cnt)
print(ans)

