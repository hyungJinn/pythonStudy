import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
melted_graph = [[0] * M for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def dfs(y, x):
    visit[y][x] = True
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < N and 0 <= nx < M and not visit[ny][nx]:
            if graph[ny][nx] != 0:
                graph[ny][nx] += 1
            else:
                dfs(ny, nx)


cheese = []
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if graph[i][j] == 1:
            cheese.append([i, j])

ans = 0
while cheese:
    
    visit = [[False] * M for _ in range(N)]
    
    dfs(0, 0)

    for i in range(len(cheese) - 1, -1, -1):
        y, x = cheese[i]
        
        if graph[y][x] >= 3:
            graph[y][x] = 0
            cheese.pop(i)
        else:
            graph[y][x] = 1
    
    ans += 1
    
print(ans)