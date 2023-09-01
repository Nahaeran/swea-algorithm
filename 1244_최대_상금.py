T = int(input())

for tc in range(1, T + 1):
    num, c = input().split()
    c = int(c)
    num_list = list(num)
    sorted_num_list = sorted(num_list, reverse=True)

    i = 0
    while c > 0:
        if num_list == sorted_num_list:
            if c % 2 == 0:
                break
            elif len(set(num_list)) < len(num_list):
                num_list = sorted_num_list
                break
            else:
                num_list[-1], num_list[-2] = num_list[-2], num_list[-1]
                break

        elif c >= len(set(num_list)) - 1:
            num_list = sorted_num_list
            c -= len(set(num_list)) // 2

        elif i < len(num_list) - 1:
            max_n = max(num_list[i + 1:])
            max_idx = len(num_list) - num_list[::-1].index(max_n) - 1
            num_list[i], num_list[max_idx] = num_list[max_idx], num_list[i]
            for j in range(len(num_list)):
                if num_list[j] == sorted_num_list[j]:
                    pass
                else:
                    i = j
                    break
            else:
                i += 1
            c -= 1

    print(f'#{tc} {"".join(num_list)}')
