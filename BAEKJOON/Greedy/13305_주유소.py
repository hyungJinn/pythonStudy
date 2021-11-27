import sys

N = int(sys.stdin.readline().rstrip('\n'))
distances = list(map(int, input().split(" ")))
prices = list(map(int, input().split(" ")))

now_price = prices[0]
now_distance = distances[0]
result = 0
for i in range(1, N - 1):
    if now_price >= prices[i]:
        result += (now_price * now_distance)
        now_price = prices[i]
        now_distance = distances[i]
    else:
        now_distance += distances[i]
        
result += (now_price*now_distance)

print(result)