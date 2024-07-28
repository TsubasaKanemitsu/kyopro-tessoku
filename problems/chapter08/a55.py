# この問題はsetで管理しているデータをリストに変換して二分探索を実施しないと回答できない。
# PythonだとTLEになる。(TLEになるテストケース以外を通した実装を残す。)

from typing import List

Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]

def search(desk: List[int], x: int) -> int:
    l, r = -1, len(desk)
    while r - l > 1:
        m = (l + r) // 2
        if desk[m] >= x:
            r = m
        else:
            l = m
    return r

desk = set()
for query in queries:
    if query[0] == 1:
        desk.add(query[1])
    if query[0] == 2:
        desk.remove(query[1])
    if query[0] == 3:
        sord_desk = sorted(desk)
        pos = search(desk=sorted(desk), x=query[1])
        if pos == len(desk):
            print(-1)
        else:
            print(sord_desk[pos])
