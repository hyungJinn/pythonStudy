import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(node):
    visit[node] = True 
    for i in range(len(tree[node])):
        next = tree[node][i]
        if visit[next] == False:
            parents[next] = node
            dfs(next)

N = int(input())

tree = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]
parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    node_a, node_b = map(int, input().split())
    tree[node_a].append(node_b)
    tree[node_b].append(node_a)
# 1 <= node_a, node_b 

dfs(1)

for i in range(2, N + 1):
    print(parents[i])