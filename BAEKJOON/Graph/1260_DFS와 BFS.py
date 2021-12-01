import sys
input = sys.stdin.readline

def dfs(graph, node):
    
    stack = list()
    visit = list()
    
    stack.append(node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            graph[node].sort()
            stack.extend(reversed(graph[node])) # like stack
    return visit

def bfs(graph, node):
    
    queue = list()
    visit = list()
    
    queue.append(node)
    
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            graph[node].sort()
            queue.extend(graph[node]) # like queue
    return visit


N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    node_a, node_b = map(int, input().split())
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)
    
visit = dfs(graph, V)
for i in visit:
    print(i, end=" ")
print()

visit = bfs(graph, V)
for i in visit:
    print(i, end=" ")