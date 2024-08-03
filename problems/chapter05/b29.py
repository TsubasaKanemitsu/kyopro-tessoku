def power(a: int, b:int, m: int) -> int:
    p = a
    ans = 1
    while b > 0:
        if b & 1:
            ans = (ans * p) % m
        p = (p * p) % m
        b >>= 1
    return ans

a, b = list(map(int, input().split()))

print(power(a, b, 10 ** 9 + 7))