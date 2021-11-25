import sys

S = int(sys.stdin.readline().rstrip('\n'))

s_sum = 1;
cnt = 1;

while s_sum < S:
    cnt += 1
    s_sum += cnt
    
    if s_sum > S:
        cnt -= 1

print(cnt)