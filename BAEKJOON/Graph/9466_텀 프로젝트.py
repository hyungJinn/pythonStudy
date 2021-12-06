import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def dfs(node):
    global result
    visit[node] = True
    cycle.append(node)
    next = graph[node]
    
    if not visit[next]:
        dfs(next)
    else:
        if next in cycle:
            result += cycle[cycle.index(next):]
        return

for _ in range(int(input())):
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    
    visit = [False] * (N + 1)
    result = []
    
    for i in range(1, N + 1):
        if not visit[i]:
            cycle = []
            dfs(i)
            
    print(N - len(result))