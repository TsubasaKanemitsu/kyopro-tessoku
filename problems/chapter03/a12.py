from typing import List

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

# X秒後の印刷枚数は (X // A_1 + X // A_2 + ... + X // A_n)より、
# (X // A_1 + X // A_2 + ... + X // A_n) >= Kを満たす最小値のXを求めればいい

def search(K: int, A: List) -> int:
    l, r = 0, 10 ** 18 + 1

    while r - l > 1:
        m = (l + r) // 2
        
        chirashi_num = sum([m // a for a in A])
        if chirashi_num >= K:
            r = m
        else:
            l = m

    return r

ans = search(K=K, A=A)
print(ans)