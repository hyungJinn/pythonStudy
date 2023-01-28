# 9093_단어 뒤집기.py
# https://star7sss.tistory.com/249
# Data Structures

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    str = list(input().split()) # 굳이 rstrip() 필요 없는 거 같은데.
    for s in str:
        print(s[::-1], end=" ") # [::-1] 거꾸로 뒤집은 결과를 의미.
    print()