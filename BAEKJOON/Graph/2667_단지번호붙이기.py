import sys
input = sys.stdin.readline

def dfs(start):
    

N = int(input())
apart_complex = []
for _ in range(N):
    apart_complex.append(list(map(int, input().rstrip('\n'))))
    
for i in range(N):
    for j in range(N):
        if apart_complex[i][j] == 1:
            