for test_case in range(1, 11):
    n = int(input())
    li = list(map(int, input().split()))

    result = 0
    # 왼쪽 2칸, 오른쪽 2칸은 건물x
    for i in range(2, n - 2):
        # 주변 2칸 건물 중 가장 큰 건물을 찾음
        around_max = max(li[i-2], li[i-1], li[i+1], li[i+2])
        # 만약 주변 가장 큰 건물보다 검사 중인 건물이 크다면
        if li[i] > around_max:
            # 검사하는 건물 - 주변 큰 건물만큼이 조망권이 확보된 세대임
            result += (li[i] - around_max)
    print(f'#{test_case} {result}')