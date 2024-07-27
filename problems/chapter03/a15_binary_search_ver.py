from typing import List

N = int(input())
A = list(map(int, input().split()))
B = sorted(list(set(A)))

def search(a: int, B: List[int]) -> int:
    l, r = -1, len(B) - 1

    while r - l > 1:
        m = (l + r) // 2

        if B[m] >= a:
            r = m
        else:
            l = m

    return r

for a in A:
    idx = search(a=a, B=B)
    print(idx + 1, end=" ")
print()
