from typing import List

N = int(input())

# 考察
# 1 <= N <= 10 ^ 6より
# xは0 < x < 10 ^ 2未満と考えられる

# def search(N: int) -> int:
#     l, r = 0.0, 100.0
#     for _ in range(20):
#         x = (l + r) / 2
#         n = x * x * x + x
#         if n > N:
#             r = x
#         else:
#             l = x
#     return x

def search(N: int) -> int:
    l, r = 0.0, 100.0
    while r - l > 0.001:
        x = (l + r) / 2
        n = x * x * x + x
        if n > N:
            r = x
        else:
            l = x
    return x

print(search(N=N))