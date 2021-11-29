N, K = map(int, input().split())
appliances = list(map(int, input().split()))

cnt = 0
j = 0
result = []
for idx, val in enumerate(appliances):
    if j == N:
        if val not in result:
            latest_idx = 0
            change_idx = 0
            for index, value in enumerate(result):
                temp = 0
                if value in appliances:
                    temp = appliances.index(value)
                else:
                    temp = 101 # max_K
                
                if latest_idx <= temp:
                    latest_idx = temp
                    change_idx = index
                    
            result[change_idx] = val
            cnt += 1
    else:
        if val not in result:
            result.append(val)
            j += 1
            
    appliances[idx] = 0
    
print(cnt)