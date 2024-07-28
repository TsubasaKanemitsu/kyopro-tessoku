from collections import defaultdict
N = int(input())
A = [int(input()) for _ in range(N)]

counter = defaultdict(int)
ans = 0
for a in A:
    ans += counter[a]
    counter[a] += 1
print(ans)

# 想定外の解法
# for a in A:
#     counter[a] += 1

# key = list(set(A))
# ans = 0
# for k in key:
#     cnt = counter[k]
#     ans += cnt * (cnt - 1) // 2
# print(ans)