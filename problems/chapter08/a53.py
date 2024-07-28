import heapq

Q = int(input())
query = [list(input().split()) for _  in range(Q)]

priority_queue = []
for i in range(Q):
    q = query[i]
    if q[0] == "1":
        heapq.heappush(priority_queue, int(q[1]))
    if q[0] == "2":
        print(priority_queue[0])
    if q[0] == "3":
        heapq.heappop(priority_queue)
