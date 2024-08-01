import math

Q = int(input())
X = [int(input()) for _ in range(Q)]

def is_prime(x: int) -> bool:
    i = 2
    flg = True
    while i <= math.sqrt(x):
        if x % i == 0:
            flg = False            
            break
        i += 1

    return flg

for x in X:
    flg = is_prime(x)
    if flg:
        print("Yes")
    else:
        print("No")
