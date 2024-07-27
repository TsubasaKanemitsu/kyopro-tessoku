N = int(input())
S = input()

ret1 = [0] * N
ret2 = [0] * N

streak1 = 1
ret1[0] = 1
for i in range(N - 1):
    if S[i] == 'A':
        streak1 += 1
    if S[i] == 'B':
        streak1 = 1
    ret1[i + 1] = streak1

streak2 = 1
ret2[N - 1] = 1
for i in reversed(range(N - 1)):
    if S[i] == 'A':
        streak2 = 1
    if S[i] == 'B':
        streak2 += 1
    # 逆順から始める場合、A or Bで初期値が変わるのでres2[i]から更新を行なっている。
    # 最初がBであれば、BB or ABであり、一番右端のBは2以上でなければならない。逆にAA or BAであれば、Aは1でいい。
    ret2[i] = streak2

ans = 0
for i in range(N):
    ans += max(ret1[i], ret2[i])
print(ans)