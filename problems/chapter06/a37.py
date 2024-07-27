N, M, B = list(map(int, input().split()))
A = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = N * sum(C) + M * sum(A) + N * M * B
print(ans)