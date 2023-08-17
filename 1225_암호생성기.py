for tc in range(1, 11):
    tc = int(input())
    Q = list(map(int, input().split()))

    temp = 1
    while Q[-1] != 0:
        num = Q.pop(0)
        num -= temp
        if num < 0:
            Q.append(0)
            break
        else:
            Q.append(num)
        temp += 1
        if temp == 6:
            temp = 1

    print(f'#{tc} {" ".join(map(str, Q))}')