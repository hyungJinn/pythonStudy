def dfs(i, j):
    if j == (C - 1):
        return True
    
    for d in directions:
        if 0 <= (i + d) < R and gas_map[i + d][j + 1] == '.' and not visit[i + d][j + 1]:
            visit[i + d][j + 1] = True
            if dfs(i + d, j + 1):
                return True
    return False

R, C = map(int, input().split())
gas_map = [list(input().rstrip()) for _ in range(R)]
visit = [[False] * C for _ in range(R)]

cnt = 0
directions = [-1, 0, 1]

for i in range(R):
    if gas_map[i][0] == '.':
        if dfs(i, 0):
            cnt += 1

print(cnt)

