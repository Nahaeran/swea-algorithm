for tc in range(1, 11):
    TC = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    
    row_sum_list = []
    col_sum_list = []
    digonal_sum= [0, 0]
    
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += matrix[i][j]
        row_sum_list.append(row_sum)

    for j in range(100):
        col_sum = 0
        for i in range(100):
            col_sum += matrix[i][j]
        col_sum_list.append(col_sum)
    
    for i in range(100):
        digonal_sum[0] += matrix[i][i]
        digonal_sum[1] += matrix[i][99 -  i]
    
    result = max(max(row_sum_list), max(col_sum_list), max(digonal_sum))
    print(f'#{TC} {result}')