import sys
input = sys.stdin.readline

def dfs(node):
    visit[node] = True
    for i in range(len(tree[node])):
        next = tree[node][i]
        if visit[next] == False:
            cnt[next] = (cnt[node] + 1)
            dfs(next)

N = int(input())
target = list(map(int, input().split()))
M = int(input())

tree = [[] for _ in range(N + 1)]
cnt = [-1 for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]

for _ in range(M):
    node_a, node_b = map(int, input().split())
    tree[node_a].append(node_b)
    tree[node_b].append(node_a)

cnt[target[0]] = 0
dfs(target[0])

print(cnt[target[1]])