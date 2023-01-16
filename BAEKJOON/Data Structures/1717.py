# https://alpyrithm.tistory.com/117
# https://blog.naver.com/ndb796/221230967614

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
# 인덱스 번호는 '노드 번호'를 의미한다.
# 첫 번째 행은 '부모 노드 번호'를 의미한다.

def find(target):
    if target == parent[target]:
        return target
    
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)
    
    # 부모를 합칠 때는 일반적으로 더 작은 값 쪽으로 합친다.
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    flag, a, b = map(int, input().split())
    if flag:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)