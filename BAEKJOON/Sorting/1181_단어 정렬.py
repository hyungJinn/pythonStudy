# https://www.notion.so/1181_-py-4c6a60970ad4442d9713c14a11b648f0

import sys
input = sys.stdin.readline

N = int(input())

word = []
for i in range(N):
    word.append(input().rstrip())
# print(word)

set_word = list(set(word))
# print(set_word)

sorted_word = []
for i in set_word:
    sorted_word.append((len(i), i))
# print(sorted_word)

result = sorted(sorted_word)
# print(result)

for len_word, word in result:
    print(word)