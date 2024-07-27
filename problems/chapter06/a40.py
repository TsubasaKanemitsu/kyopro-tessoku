from collections import Counter
from math import comb
N = int(input())
A = list(map(int, input().split()))

a_counter = Counter(A)

ans = 0
for numer, cnt in a_counter.items():
    if cnt >= 3:
        ans += comb(cnt, 3)
print(ans)