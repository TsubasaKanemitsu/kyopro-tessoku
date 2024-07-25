from typing import List

# めぐる式で実装
# l, rを-1, len(A)で初期化している理由
# -> 今回は x <= A[i]を満たす条件の中の最小値の位置を特定し、その位置をx未満のAの要素数として扱おうとしている。
# -> そのため、半開区間としてl, rを扱う場合、rは0 <= r len(A)となって欲しいため、
# -> lは-1, rはlen(A)としている。
def search(x: int, A: List[int]) -> bool:
    # 整数x以上となるAの整数のうち、最小値のインデックスを返す
    l = -1
    r = len(A)

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
# -> 配列AのX_i以上の最小値の存在する位置を特定し、要素数を考える。
min_A = A[0]
max_A = A[-1]
for x in X: 
    idx = search(x=x, A=A)
    print(idx)
