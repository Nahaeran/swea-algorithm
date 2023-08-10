def count_paper(num):
    a1 = 1
    a2 = 3
    if num % 2 == 1:
        n = num // 2
        sum_seq = 4 * (4 ** n - 1) // 3
        result = a1 + sum_seq
        return result
    else:
        n = num // 2 - 1
        sum_seq = 8 * (4 ** n - 1) // 3
        result = a2 + sum_seq
        return result


T = int(input())

for tc in range(1, T+1):
    N = int(input()) // 10
    print(f'#{tc} {count_paper(N)}')