import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(y, x):
    global cnt
    
    if 0 > y or y >= N or 0 > x or x >= M:
        return False
    
    if graph[y][x] == 1:
        
        graph[y][x] = 0
        cnt += 1
        
        dfs(y + 1, x)
        dfs(y, x + 1)
        dfs(y - 1, x)
        dfs(y, x - 1)
        
        return True
            
    return False


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 방향벡터를 사용해서 for문을 돌리면 메모리 초과 에러 메시지가 나온다.
#dy = [1, 0, -1, 0]
#dx = [0, 1, 0, -1]

result = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            result.append(cnt)

if len(result) == 0:
    print(len(result))
    print(0)
else:
    print(len(result))
    print(max(result))