# https://star-mind-f7b.notion.site/12865-ad77a5ad2e7e45b483cf26862b580a4b

N, K = map(int, input().split())

List = [[0, 0]] # I wanted to start from List[1]
DP = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(N):
    List.append(list(map(int, input().split())))
    
for i in range(1, N + 1):
    for j in range(1, K + 1):
        W = List[i][0]
        V = List[i][1]
        
        if j < W:
            DP[i][j] = DP[i - 1][j]
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - W] + V)
            # This recurrence relation is very important

print(DP[N][K])