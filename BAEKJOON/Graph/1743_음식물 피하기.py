import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(y, x, cnt):
    forest[y][x] = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 1 <= ny <= N and 1 <= nx <= M:
            if forest[ny][nx] == 1:
                cnt = dfs(ny, nx, cnt + 1)
    
    return cnt


N, M, K = map(int, input().split())
forest = [[0]*(M+1) for _ in range(N+1)]

for i in range(K):
    r, c = map(int, input().split())
    
    forest[r][c] = 1

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

answer = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if forest[i][j] == 1:
            answer = max(answer, dfs(i, j, 1))

print(answer)