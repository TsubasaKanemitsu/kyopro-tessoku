from typing import List

N = int(input())

def eratos_tenesu(N: int) -> List[bool]:
    deleted = [False] * (N + 1)

    i = 2
    LIMIT = int(N ** 0.5)
    for i in range(2, LIMIT + 1):
        if deleted[i]:
            continue
        for j in range(i * 2, N + 1, i):
            deleted[j] = True
    
    return deleted

deleted = eratos_tenesu(N)
for i in range(2, N + 1):
    if not deleted[i]:
        print(i)