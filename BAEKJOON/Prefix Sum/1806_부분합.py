# https://star-mind-f7b.notion.site/1806_-9e42da2da22148cb9a42261c34ed4767

import sys
input = sys.stdin.readline

N, S = map(int, input().split()) #N(10 ≤ N < 100,000)
nums = list(map(int, input().split()))
left, right = 0, 0
s = nums[0] #for the situation that nums[0] by itself is bigger than S
ans = 100001 #최대값이 100,000이다, 현재 최소 길이를 구하는 중

while True:
    # checking if s from left to right is bigger than S
    if s >= S:
        s -= nums[left]
        ans = min(ans, right - left + 1) #initialize ans
        left += 1
    else:
        right += 1
        
        if right == N:
            break
        
        s += nums[right]

print(0) if ans == 100001 else print(ans)