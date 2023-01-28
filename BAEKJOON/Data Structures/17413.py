# 17413_단어 뒤집기 2.py
# https://star7sss.tistory.com/391
# Data Structures - Stack

str = list(input()) # 뒤에 공백 문자 없다. ['a', 'b', 'c']
stack = []
result = ''
flag = False

for s in str:
    # 공백이면 stack을 비움
    if s == ' ':
        while stack:
            result += stack.pop()
        result += s
    
    # 태그 안 단어는 뒤집지 않음
    elif s == '<':
        while stack:
            result += stack.pop()
        flag = True
        result += s
    
    elif s == '>':
        flag = False
        result += s
    
    elif flag:
        result += s
    
    # 태그 밖 단어는 뒤집음
    else:
        stack.append(s)
        
# 출력
while stack:
    result += stack.pop()
print(result)