# https://hongcoding.tistory.com/114

import sys
input = sys.stdin.readline

stack = []
tmp = 1
result = 0
ipt = list(input().rstrip())

for i in range(len(ipt)):
    if ipt[i] == "(":
        stack.append(ipt[i])
        tmp *= 2
    
    elif ipt[i] == "[":
        stack.append(ipt[i])
        tmp *= 3
    
    elif ipt[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        if ipt[i - 1] == "(":
            result += tmp
        
        stack.pop()
        tmp //= 2
    
    else:
        if not stack or stack[-1] == "(":
            result = 0
            break
        if ipt[i - 1] == "[":
            result += tmp
        
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(result)