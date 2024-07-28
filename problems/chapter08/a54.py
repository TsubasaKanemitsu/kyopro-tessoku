from collections import defaultdict
Q = int(input())
query = [list(input().split()) for _ in range(Q)]

record = defaultdict(int)
for i in range(Q):
    q = query[i]
    if q[0] == "1":
        record[q[1]] = q[2]
    if q[0] == "2":
        print(record[q[1]])
