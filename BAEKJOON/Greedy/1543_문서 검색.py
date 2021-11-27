import sys

document = sys.stdin.readline().rstrip("\n")
word = sys.stdin.readline().rstrip("\n")

cnt = 0
word_len = len(word)
start_idx = 0
find_idx = 0

while document.find(word, start_idx) >= 0:
    cnt += 1
    find_idx = document.find(word, start_idx)
    start_idx = (find_idx + word_len)

print(cnt)