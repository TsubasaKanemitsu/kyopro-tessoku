from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

order_dict = defaultdict(int)
max_val = 0
for i, a in enumerate(sorted(list(set(A)))):
    order_dict[a] = i + 1

for a in A:
    print(order_dict[a], end=" ")
print()
