T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
     
    # 합계들을 저장하는 리스트 초기화
    sum_list = []
    # 총 n-m+1개의 부분 리스트가 나옴
    for i in range(n-m+1):
        temp = 0
        # 구간 내의 요소를 임의의 합(temp)에 더해감
        for j in range(m):
            temp += li[i+j]
        # 만들어진 합을 sum_list에 추가
        sum_list.append(temp)
    # 구간 합의 최대, 최소를 찾음
    max_sum = max(sum_list)
    min_sum = min(sum_list)
    print(f'#{test_case} {max_sum - min_sum}')