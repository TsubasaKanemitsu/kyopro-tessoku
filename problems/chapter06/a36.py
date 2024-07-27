N, K = list(map(int, input().split()))

if K % 2 == 1:
    print("No")
else:
    if K >= 2 * (N - 1):
        print("Yes")
    else:
        print("No")