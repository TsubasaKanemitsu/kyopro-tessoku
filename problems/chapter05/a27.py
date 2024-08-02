A, B = list(map(int, input().split()))

def gcd(a: int, b: int) -> int:
    if b > a:
        tmp = a
        a = b
        b = tmp
    
    if a % b == 0:
        return b
    return gcd(b, a % b)

print(gcd(A, B))