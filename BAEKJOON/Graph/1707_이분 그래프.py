import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(vertex):
    visit[vertex] = True
    
    for next in graph[vertex]:
        if visit[next] == False:
            colors[next] = colors[vertex] * -1
            if not dfs(next):
                return False
        elif colors[next] == colors[vertex]:
                return False
    return True            

K = int(input())

for i in range(K):
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V+1)]
    visit = [False] * (V+1)
    colors = [1] * (V+1)
    
    flag = True
 
    for i in range(E):
        vertex_a, vertex_b = map(int, input().split())
        graph[vertex_a].append(vertex_b)
        graph[vertex_b].append(vertex_a)
    
    for i in range(1, V + 1):
        if visit[i] == False:
            flag = dfs(i)
            if not flag:
                break
    
    print("YES" if flag else "NO")