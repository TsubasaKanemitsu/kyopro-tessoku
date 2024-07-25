N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

left = 0
right = len(A) - 1

while left <= right:
    m = (left + right) // 2

    if A[m] > X:
        right = m - 1
    elif A[m] < X:
        left = m + 1
    else:
        print(m + 1)
        exit()
