import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
melted_graph = [[0] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cheese = []
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if graph[i][j] == 1:
            cheese.append([i, j])

cnt = 0
while cheese:
    cnt += 1
    
    melted_cheese = []
    for i in range(len(cheese) - 1, -1, -1):
        y, x = cheese[i] # cordinate(좌표)
        
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            
            if graph[ny][nx] == 0:
                melted_graph[y][x] += 1
            
        if melted_graph[y][x] > 0:
            melted_cheese.append((y, x, i))
    
    for y, x, i in melted_cheese:
        if melted_graph[y][x] >= 2:
            graph[y][x] -= 1
            cheese.pop(i)
        
        melted_graph[y][x] = 0

print(cnt)