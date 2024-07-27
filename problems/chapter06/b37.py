# f(1) + f(2) + ... +  f(N)を求める
# 通常：f(N)の和を求めて足し合わせる方法を考えるが、これだと計算量がO(N)になり、間に合わないので高速化の検討が必要である。
# 高速化：主客転倒テクニック。f(N)を求めていくのではなく、0 <= x <= Nの間で各桁の数値が何回出現するかを求めて、足し合わせるという風に言い換える。

N = input()

# 10のN乗を求める
power10 = [0] * (len(N) + 1)
for i in range(len(N) + 1):
    power10[i] = 10 ** i


R = [[0] * 10 for _ in range(len(N))]
for i in range(len(N)):
    # 下からi桁目の数字
    digit = (int(N) // power10[i]) % 10
    for j in range(10):
        if j < digit:
            R[i][j] = int(N) // power10[i + 1] * power10[i] + power10[i]
        if j == digit: 
            R[i][j] = int(N) // power10[i + 1] * power10[i] + int(N) % power10[i] + 1
        if j > digit:
            R[i][j] = int(N) // power10[i + 1] * power10[i]

ans = 0
for i in range(len(N)):
    for j in range(10):
        ans += j * R[i][j]
print(ans)
