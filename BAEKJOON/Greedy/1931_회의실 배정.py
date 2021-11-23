import sys

N = int(sys.stdin.readline())

temp = []
confs = []
for i in range(0, N):
    confs.append(list(map(int, sys.stdin.readline().split())))
confs.sort(reverse=True)

cnt = 1
now = confs[0][0]
for i in range(1, N):
    if now >= confs[i][1]:
        cnt += 1
        now = confs[i][0]
    
print(cnt)