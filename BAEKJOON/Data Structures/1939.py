# 1939_중량제한.py
# https://hbj0209.tistory.com/132
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
        
def check(a, b):
    return find(a) == find(b)

N, M = map(int, input().split())
graph = []
parents = [i for i in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append([-C, A, B])

ta, tb = map(int, input().split())

graph.sort()
for i in graph:
    c, a, b = i[0], i[1], i[2]
    c = abs(c)
    union(a, b)
    
    if check(ta, tb):
        print(c)
        break