import sys
input = sys.stdin.readline

def dfs(node):
    global N, M
    count = 1
    visit = [[False] * M for _ in range(N)]
    visit[node[0]][node[1]] = True
    
    s = [node]
    
    while s:
        now = s.pop() # now == [y, x]
        
        for i in range(4):
            ny = now[0] + d[i][0]
            nx = now[1] + d[i][1]
            
            if not visit[ny][nx] and graph[ny][nx] != 0:
                s.append([ny, nx])
                visit[ny][nx] = True
                count += 1
    return count


N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
melted_graph = [[0] * M for _ in range(N)]

d = [[-1, 0], [0, 1], [1, 0], [0, -1]] 
# d = [[y, x], ..., ]

ice = []
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if graph[i][j] != 0:
            ice.append([i, j])

ans = 0
cnt = 0   
while ice:
    # 두 덩어리 이상으로 분리된 입력 값이 주어졌을 때
    if len(ice) != dfs(ice[0]):
        ans = cnt
        break
    
    # after one year
    cnt += 1
    
    melted_ice = []
    for i in range(len(ice) - 1, -1, -1):
        y, x = ice[i] # cordinate
        
        for dir in range(4):
            next_y = y + d[dir][0]
            next_x = x + d[dir][1]
            
            if graph[next_y][next_x] == 0:
                melted_graph[y][x] += 1
            
        if melted_graph[y][x] > 0:
            melted_ice.append((y, x, i))
    
    for y, x, i in melted_ice:
        graph[y][x] -= melted_graph[y][x]
        if graph[y][x] <= 0:
            graph[y][x] = 0
            ice.pop(i)
        
        melted_graph[y][x] = 0

print(ans)
