# 1918_후위 표기식.py
# https://pannchat.tistory.com/entry/파이썬-백준-후위표기식-python
# Data Structures - Stack

import sys
input = sys.stdin.readline

infix = list(input())
stack = []
result = ''

for i in infix:
    if i.isalpha():
        result += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == "*" or stack[-1] == '/'):
                result += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
            
while stack:
    result += stack.pop()

print(result)