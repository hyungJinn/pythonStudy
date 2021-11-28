import sys

N = int(sys.stdin.readline().rstrip('\n'))
scores = []

temp = 0
for i in range(N):
    temp = int(sys.stdin.readline().rstrip('\n'))
    scores.append(temp)

scores.reverse()
now_element = scores[0]
scores_len = len(scores)
cnt = 0
gap = 0
for i in range(1, N):
    gap = now_element - scores[i]
    if gap <= 0:
        gap = (gap * -1) + 1
        scores[i] -= gap
        cnt += gap
    
    now_element = scores[i]

print(cnt)