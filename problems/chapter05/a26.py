import math

Q = int(input())
X = [int(input()) for _ in range(Q)]

def is_prime(x: int) -> bool:
    for i in range(2, x ** 0.5 + 1):
        if x % i == 0:
            return False
    return True

for x in X:
    flg = is_prime(x)
    if flg:
        print("Yes")
    else:
        print("No")
