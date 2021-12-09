# I referred to this site, https://cotak.tistory.com/66.

import sys, itertools, collections
input = sys.stdin.readline

N = int(input())
people = [int(x) for x in input().split()]
graph = collections.defaultdict(list)
result = float('inf')

for i in range(N):
    _input = list(map(int, input().split()))
    for j in range(1, _input[0] + 1):
        graph[i].append(_input[j] - 1)


def bfs(same):
    start = same[0]
    q = collections.deque([start])
    
    visit = set([start])
    _sum = 0
    while q:
        v = q.popleft()
        _sum += people[v]
        for u in graph[v]:
            if u not in visit and u in same:
                q.append(u)
                visit.add(u)
    return _sum, len(visit)
    
    
for i in range(1, N//2 + 1):
    # range(N) == range(0, N) == [0, 1, 2, 3, 4, ..., N]
    combis = list(itertools.combinations(range(N), i))
    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(N) if i not in combi])
        if v1 + v2 == N:
            result = min(result, abs(sum1 - sum2))

# float('inf') == 양의 무한대
if result != float('inf'):
    print(result)
else:
    print(-1)