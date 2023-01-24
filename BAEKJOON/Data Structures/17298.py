# 17298_오큰수.py
# https://hooongs.tistory.com/329
# Data Structures - Stack

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
seq = list(map(int, input().split()))

NGEs = [-1] * N # 오큰수, [-1, -1, ..., -1]
S = deque() # stack

for i in range(N):
    while S and (S[-1][0] < seq[i]):
        tmp, idx = S.pop()
        NGEs[idx] = seq[i]
    S.append([seq[i], i])

print(*NGEs)

# O(N^2)이 걸릴수도 있는 문제를 스택을 사용해 O(N)에 가깝게 만드는 문제.

# Ai에 대한 오큰수 = NGEs(Ai) = 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수

# 왼쪽에서부터 값을 스택에 넣으면서 알고리즘을 진행해나간다.
# 스택에 가장 위에 있는 값이 현재의 값보다 작거나 스택이 빌때까지 pop연산을 해준다.
# (현재의 값이 스택에 가장 위에 있는 값보다 작거나 스택이 비어 있으면 push연산을 한다.)
# 스택의 가장 위의 값이 pop이 되는 순간, 바로 해당 인덱스의 오큰수가 현재 값이 된다.