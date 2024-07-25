from typing import List

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

def search(a: int, l: int, N: int, K: int) -> int:
    r = len(A)

    while r - l > 1:
        m = (l + r) // 2
        if A[m] <= a + K:
            l = m
        else:
            r = m
    return l

cnt = 0
for i in range(N):
    # A[t] <= A[i] + KとなるA[t]を求める
    # 二分探索（最小値の最大化）
    t = search(a=A[i], l=i, N=N, K=K)
    cnt += t - i
print(cnt)