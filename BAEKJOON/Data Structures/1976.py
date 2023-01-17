# https://my-coding-notes.tistory.com/332

import sys
# sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(target):
    if target != parent[target]:
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

N, M = int(input()), int(input())
parent = [i for i in range(N+1)]
# 인덱스 번호는 '노드 번호'를 의미한다.
# 첫 번째 행은 '부모 노드 번호'를 의미한다.
# the number of city start from 1 to N
for i in range(1, N+1):
    link = list(map(int, input().split()))
    for j in range(N):
        if link[j] == 1:
            union(i, j+1)

path = list(map(int, input().split()))
for i in range(M):
    if parent[path[i]] != parent[path[0]]:
        print('NO')
        break
else:  
    print('YES')