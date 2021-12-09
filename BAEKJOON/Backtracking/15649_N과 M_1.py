import sys, itertools
input = sys.stdin.readline

N, M = map(int, input().split())
result = list(itertools.permutations(range(1, N + 1), M))

for i in result:
    print(*i)