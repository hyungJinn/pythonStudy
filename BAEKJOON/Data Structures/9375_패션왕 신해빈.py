# https://hongcoding.tistory.com/60
# https://aia1235.tistory.com/29

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    clothes = {}
    result = 1
    
    N = int(input())
    for _ in range(N):
        name, type = input().rstrip().split()
        
        if not type in clothes:
            clothes[type] = 1
        else:
            clothes[type] += 1

    for i in clothes:
        result *= (clothes[i] + 1)

    print(result - 1)
    