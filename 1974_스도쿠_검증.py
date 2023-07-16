T = int(input())
for test_case in range(T):
    li = [list(map(int, input().split())) for i in range(9)]
    answer = 362880
    result = 0
    for i in range(9):
        mul_r = 1
        mul_c = 1

        for j in range(9):
            mul_r *= li[i][j]
            mul_c *= li[j][i]
            mul_b = 1
            if i % 3 == 0 and j % 3 == 0:
                for k in range(3):
                    for s in range(3):
                        mul_b *= li[i + k][j + s]
                if mul_b == answer:
                    result += 1

        if mul_r == answer:
            result += 1
        if mul_c == answer:
            result += 1

    print("#" + str(test_case + 1), 1) if result == 27 else print(
        "#" + str(test_case + 1), 0
    )
