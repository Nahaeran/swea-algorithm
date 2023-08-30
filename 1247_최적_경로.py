def dfs(idx, lastX, lastY, distance):
    global min_count 
    if min_count < distance:
        return
    if idx == n:
        distance += abs(lastX - home[0]) + abs(lastY - home[1])
        min_count = min(distance, min_count)
        return
    for i in range(n):
        if check_list[i]:
            check_list[i] = False
            temp = distance + abs(lastX - positions[i][0]) + abs(lastY - positions[i][1])
            dfs(idx+1, positions[i][0], positions[i][1], temp)
            check_list[i] = True


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    li = list(map(int, input().split()))
    check_list = [True for _ in range(n)]
    positions = []
    for i in range(0, len(li), 2):
        positions.append(li[i:i+2])
        
    home = positions.pop(0)
    company = positions.pop(0)
    min_count = 10000
    
    dfs(0, company[0], company[1], 0)
    print(f'#{tc} {min_count}')