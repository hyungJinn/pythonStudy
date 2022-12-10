# https://somjang.tistory.com/entry/BaekJoon-4153%EB%B2%88-%EC%A7%81%EA%B0%81%EC%82%BC%EA%B0%81%ED%98%95-Python

import sys
import math
input = sys.stdin.readline

while True:
    input_value = input().rstrip()
    
    if input_value == "0 0 0":
        break
    
    triangle = list(map(int, input_value.split()))
    triangle.sort()
    
    if int(math.sqrt(pow(triangle[0], 2) + pow(triangle[1], 2))) == triangle[2]:
        print("right")
    else:
        print("wrong")
    