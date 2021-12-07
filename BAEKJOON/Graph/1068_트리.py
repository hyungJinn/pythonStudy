import sys
input = sys.stdin.readline

def dfs(node):
    global answer
    
    if not tree[node]:
        answer += 1
        return
    
    for j in tree[node]:
        dfs(j)

N = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(N)]
K = int(input())

root = 0
for i in range(N):
    if arr[i] == -1:
        root = i
        continue
    if i == K or arr[i] == K:
        continue
    tree[arr[i]].append(i)

answer = 0
if root != K:
    dfs(root)
print(answer)