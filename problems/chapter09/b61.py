N, M = list(map(int, input().split()))
friend_cnt = [0] * N
for i in range(M):
    a, b = list(map(int, input().split()))
    friend_cnt[a - 1] += 1
    friend_cnt[b - 1] += 1

max_val = -1
max_student = -1
for i in range(N):
    if max_val < friend_cnt[i]:
        max_val = friend_cnt[i]
        max_student = i
print(max_student + 1)