# 1026_보물.py
# https://gudwns1243.tistory.com/55
# Greedy

import sys
input = sys.stdin.readline

# S = A[0] x B[0] + … + A[N-1] x B[N-1]
# S's minimum

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
A.sort()
for i in range(N):
    a = A[i]
    b = B.pop(B.index(max(B)))
    
    result += (a * b)

print(result)

# A와 B를 서로 가장 큰 수와 가장 작은 수 끼리 곱해서 더하면 되는 문제.
# 조건, B를 재정렬하면 안 된다.
# A는 정렬을 해주어 순서대로 뽑고 B는 pop()을 이용해 최대값부터 뽑아서 서로 곱해서 구한다.