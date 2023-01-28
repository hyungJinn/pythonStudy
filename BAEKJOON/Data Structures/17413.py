# 17413_단어 뒤집기 2.py
# Data Structures - Stack

str = list(input())
stack = []
result = ''
flag = False

for s in str:
    if flag == False:
        if s == '<':
            flag = True
            while stack:
                result += stack.pop()
            stack.append(s)
        elif s == ' ':
            while stack:
                result += stack.pop()
            result += s
        else:
            stack.append(s)
            
    elif flag == True:
        stack.append(s)
        if s == '>':
            flag = False
            stack.reverse()
            while stack:
                result += stack.pop()

while stack:
    result += stack.pop()

print(result)