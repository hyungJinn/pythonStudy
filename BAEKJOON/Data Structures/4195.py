# 4195_친구 네트워크.py
# Union-Find 
# https://assaeunji.github.io/python/2020-05-05-bj4195/
# https://chancoding.tistory.com/50

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 함수의 목적은 최종 부모 노드를 찾는 것이다.
def find(target):
    if target != parents[target]:
        parents[target] = find(parents[target])
        
    return parents[target]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parents[b] = a
        nums[a] += nums[b]
        
T = int(input()) # Test Case
for _ in range(T):
    parents = dict()
    nums = dict()
    
    F = int(input()) # Friends
    for _ in range(F):
        a, b = input().split()
        
        if a not in parents:
            parents[a] = a
            nums[a] = 1
        if b not in parents:
            parents[b] = b
            nums[b] = 1
        
        union(a, b)
        print(nums[find(a)])
# 처음의 각각의 원소는 연결된 정보가 없기 때문에 부모로 자기 자신을 가지고 있다.
# 친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램.
# 일반적인 유니온 파인드와 다르게 숫자가 아닌 문자열이 들어가므로 친구의 숫자를 저장하기 위한 리스트를 하나 더 선언해줘야한다.
