N = input()

ans = 0
for x in range(len(N)):
    ans += (2 ** (len(N) - 1 - x)) * int(N[x])
print(ans)