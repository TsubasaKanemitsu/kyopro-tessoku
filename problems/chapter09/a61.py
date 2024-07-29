from collections import defaultdict
N, M = list(map(int, input().split()))

ans = defaultdict(set)
for i in range(M):
    a, b = list(map(int, input().split()))
    ans[a].add(str(b))
    ans[b].add(str(a))
for i in range(1, N + 1):
    ouput = ''
    ouput += str(i)
    ouput += ": {"
    ouput += ", ".join(list(ans[i]))
    ouput += "}"
    print(ouput)