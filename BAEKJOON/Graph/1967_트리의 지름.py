import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
graph = [[] * N for _ in range(N+1)]


def dfs(node, wei):
    for i in graph[node]:
        child, weight = i
        if distance[child] == -1:
            distance[child] = wei + weight
            dfs(child, wei + weight)
            

for _ in range(N - 1):
    P, C, W = map(int, input().split()) # parent, child, weight
    graph[P].append([C, W])
    graph[C].append([P, W])

# 1번 노드에서 가장 먼 곳을 찾는다.
distance = [-1] * (N + 1)
distance[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에서 가장 먼 곳을 찾는다.
start = distance.index(max(distance))
distance = [-1] * (N + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))