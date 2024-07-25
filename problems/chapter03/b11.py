from typing import List

# 整数x以上となるAの整数のうち、最小値のインデックスを返す
def search(x: int, A: List[int]) -> bool:
    l = 0
    r = len(A) - 1

    while r - l > 1 :
        m = (l + r) // 2

        if A[m] >= x:
            r = m
        else:
            l = m
    return r

N = int(input())
A = list(map(int, input().split()))

Q = int(input())
X = []
for i in range(Q):
    x = int(input())
    X.append(x)

# 昇順に並び替える
A.sort()

# 言い換え
# 配列AにはX_iより小さい要素が何個あるか。
# -> 配列AのX_i以上の最小値の存在する位置を特定し、その位置の1つ手前+1が要素数となる。
min_A = A[0]
max_A = A[-1]
for x in X: 
    if x <= min_A:
        print(0)
        continue
    if x > max_A:
        print(N)
        continue
    idx = search(x = x, A=A)
    print(idx)
