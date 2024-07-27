N = int(input())
S = input()

ans = False
for i in range(N - 2):
    if S[i] == 'R' and S[i] == S[i + 1] and S[i] == S[i + 2]:
        ans = True
    if S[i] == 'B' and S[i] == S[i + 1] and S[i] == S[i + 2]:
        ans = True

if ans:
    print("Yes")
else:
    print("No")