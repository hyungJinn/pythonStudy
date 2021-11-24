import sys

N = sys.stdin.readline().rstrip('\n') # str
arr = list(map(int, N)) # list = [int, int, int, ..., int]
arr_sum = sum(arr)

last_element = 0 # last element in array
result = 0
temp = ''
if arr_sum % 3 == 0:
    arr.sort(reverse=True)
    last_element = arr[-1]
    if last_element == 0:
        temp = ''.join(map(str, arr))
        result = int(temp)
        print(result)
    else:
        print(-1)
else:
    print(-1)