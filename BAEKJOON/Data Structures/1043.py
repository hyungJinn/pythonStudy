# https://velog.io/@insutance/파이썬-별표-Asterisk-의-역할
# https://my-coding-notes.tistory.com/471
# 1043_거짓말.py
# Union-Find

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(target):
    if target != parents[target]:
        parents[target] = find(parents[target])
    
    return parents[target]
    
def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

N, M = map(int, input().split())
parents = [i for i in range(N+1)]
_,*t = map(int, input().split())
# 진실을 아는 사람의 부모 노드는 0으로 통일했다.
# >>> 4 1 2 3 4
# _ = 4, t = [1, 2, 3, 4]
for i in t:
    parents[i] = 0
    
parties = []
for _ in range(M):
    p,*q = map(int, input().split())
    # >>> 2 1 5
    # p = 2, q = [1, 5]
    parties.append(q)
    if p == 1:
        continue
    
    # 만난 적 있는 사람들끼리 유니온 파인드
    for i in range(p - 1):
        union(q[i], q[i+1])

result = 0
for party in parties:
    for i in party:
        if find(parents[i]) == 0:
            break
    else:
        result += 1

print(result)  