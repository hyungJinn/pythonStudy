# https://rujang.tistory.com/entry/%EB%B0%B1%EC%A4%80-2439%EB%B2%88-%EB%B3%84-%EC%B0%8D%EA%B8%B0-2-CC#:~:text=%23%EC%A0%91%EA%B7%BC%EB%B0%A9%EB%B2%95,%EC%A1%B0%EA%B1%B4%EB%AC%B8%EC%9C%BC%EB%A1%9C%20%EC%B6%9C%EB%A0%A5%ED%95%B4%EC%A3%BC%EB%A9%B4%20%EB%90%9C%EB%8B%A4.

import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    for j in range(N):
        if(j < N - i - 1): 
            print(" ", end="")
        else:
            print("*", end="")
    print()