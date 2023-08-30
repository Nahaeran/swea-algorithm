def guess(num2, num3):
    for i in range(len(num2)):
        for j in range(len(num3)):
            new_num2 = num2[:i] + str(int(not int(num2[i]))) + num2[i + 1:]
            for k in range(1, 3):
                temp = str((int(num3[j]) + k) % 3)
                new_num3 = num3[:j] + temp + num3[j+1:]
                if int(new_num2, 2) == int(new_num3, 3):
                    return int(new_num2, 2)


T = int(input())

for tc in range(1, T + 1):
    input_num2 = input()
    input_num3 = input()
    print(f'#{tc} {guess(input_num2, input_num3)}')
