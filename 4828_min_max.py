T = int(input())
 
for test_case in range(1, T + 1):
    n = int(input())
    li = list(map(int, input().split()))
     
    min_of_li = li[0]
    max_of_li = li[0]
    for i in range(n):
        if li[i] < min_of_li:
            min_of_li = li[i]
        if li[i] > max_of_li:
            max_of_li = li[i]
    result = max_of_li - min_of_li
    print(f'#{test_case} {result}')