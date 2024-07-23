A, B = list(map(int, input().split()))

for x in range(A, B + 1):
    if 100 % x == 0:
        print("Yes")
        exit()
print("No")