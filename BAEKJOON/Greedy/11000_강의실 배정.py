import sys
import heapq

N = int(sys.stdin.readline())

confs = []
for i in range(N):
    confs.append(list(map(int, sys.stdin.readline().split()))) 
    # confs[start_time][end_time]
confs.sort()

room = []
heapq.heappush(room, (confs[0][1])) 
# heapq.headpush(room, (end_time=priority))

cnt = 1
for i in range(1, N):
    if room[0] > confs[i][0]:
        heapq.heappush(room, (confs[i][1]))
        cnt += 1
    else:
        heapq.heappop(room)
        heapq.heappush(room, (confs[i][1]))
        
print(cnt)