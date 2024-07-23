N = int(input())
A = list(map(int, input().split()))

Q = int(input())
L, R = [], []
for i in range(Q):
    l, r = list(map(int, input().split()))
    L.append(l)
    R.append(r)

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

# 当たりの数をカウントしている区間長の半分未満か半分より大きいか半分であるかで
# win/lose/drawを判定する。
for i in range(Q):
    l, r = (L[i] - 1), R[i]
    if (S[r] - S[l]) > (r - l) / 2:
        print("win")
    elif (S[r] - S[l]) < (r - l) / 2:
        print("lose")
    else:
        print("draw")

# 解説の答えは、ハズレとアタリの出現回数の累積和を保持し、
# その差分を取る実装となっている。