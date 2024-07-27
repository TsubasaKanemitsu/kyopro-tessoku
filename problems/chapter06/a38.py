D, N = list(map(int, input().split()))
L, R, H = [], [], []
for i in range(N):
    l, r, h = list(map(int, input().split()))
    L.append(l - 1)
    R.append(r - 1)
    H.append(h)

min_max_roudou_zikan = [24] * D
for i in range(N):
    l, r = L[i], R[i] + 1
    min_max_time = H[i]
    for j in range(l, r):
        min_max_roudou_zikan[j] = min(min_max_roudou_zikan[j], min_max_time)
print(sum(min_max_roudou_zikan))
