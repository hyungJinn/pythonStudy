# https://my-coding-notes.tistory.com/332

import sys
# sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(target):
    if target != parents[target]:
        parents[target] = find(parents[target])
    
    return parents[target]

def union(a, b):
    a = find(a)
    b = find(b)
    
    # 부모를 합칠 때는 일반적으로 더 작은 값 쪽으로 합친다.
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

N, M = int(input()), int(input())
parents = [i for i in range(N+1)]
# 첫 번째 행(인덱스 번호)은 '노드 번호'를 의미한다.
# 두 번째 행은 '부모 노드 번호'를 의미한다.
# the number of city start from 1 to N
# range(N+1)로 하면 "0, 1, ..., N"로 리스트가 생성된다.
for i in range(1, N+1):
    link = list(map(int, input().split()))
    for j in range(N):
        if link[j] == 1:
            union(i, j+1)

path = list(map(int, input().split()))
for i in range(M):
    if parents[path[i]] != parents[path[0]]:
        print('NO')
        break
else:  
    print('YES')