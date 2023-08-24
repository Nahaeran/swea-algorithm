T = int(input())

for tc in range(1, T + 1):
    N, N_16 = input().split()
    N_2 = str(bin(int(N_16, 16)))[2:]
    add_len = 4 * int(N) - len(N_2)
    N_2 = '0' * add_len + N_2
    print(f'#{tc} {N_2}')