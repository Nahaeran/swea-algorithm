T=int(input())
for test_case in range(1, T+1):
    num = int(input())
    scores = list(map(int, input().split()))
    counts = [0]*101
    max_cnt = 0
    
    for i in range(1000):
        counts[scores[i]] +=1
    
    for i in range(101):
        if counts[i]>=max_cnt:
            max_cnt = counts[i]
            max_num = i
    
    print('#{} {}'.format(test_case, max_num))