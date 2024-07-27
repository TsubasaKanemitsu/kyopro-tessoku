N, K = list(map(int, input().split()))
S = input()
ON = 0
for i in range(N):
    if S[i] == "1":
        ON += 1
if K % 2 == ON % 2:
    print("Yes")
else:
    print("No")

