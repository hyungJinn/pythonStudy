import sys
input = sys.stdin.readline


def promising(row):
    # 같은 열이면 안 되고, 대각선상에 있어도 안 된다.
    for i in range(row):
        if board[row] == board[i] or row - i == abs(board[row] - board[i]):
            return 0
    return 1


def dfs(row):
    global ans
    
    # 마지막 행까지 수행하고 여기까지 오면 찾기 완료
    if row == N:
        ans += 1
        return
    
    for i in range(N):
        board[row] = i
        
        if promising(row):
            dfs(row + 1)
        

N = int(input())
ans = 0
board = [0] * N

dfs(0)

print(ans)
