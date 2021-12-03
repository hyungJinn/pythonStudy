import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(y, x):
    if dp[y][x]: return dp[y][x]
    
    dp[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < N and 0 <= nx < N:
            if forest[y][x] < forest[ny][nx]:
                dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)

    return dp[y][x]

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i, j))

print(answer)