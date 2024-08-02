N = int(input())
T, A = [], []
ans = 0
for i in range(N):
    t, a = list(input().split())
    if t == "+":
        ans += int(a)
    if t == "*":
        ans *= int(a) % 10 ** 4
    if t == "-":
        ans -= int(a) % 10 ** 4

    if ans < 0:
        ans += 10000

    ans %= 10000    
    print(ans)