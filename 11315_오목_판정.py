def concave(arr, N):
    for i in range(N):
        r_check = c_check = 0
        for j in range(N):
            d1_check = d2_check = 0
            if arr[i][j] == 'o':
                r_check += 1
            else:
                r_check = 0
            if arr[j][i] == 'o':
                c_check += 1
            else:
                c_check = 0

            for k in range(-2, 3):
                ni = i + k
                nj1 = j + k
                nj2 = j - k
                if 0 <= ni < N and 0 <= nj1 < N and arr[ni][nj1] == 'o':
                    d1_check += 1
                if 0 <= ni < N and 0 <= nj2 < N and arr[ni][nj2] == 'o':
                    d2_check += 1
            if r_check == 5 or c_check == 5 or d1_check == 5 or d2_check == 5:
                return 'YES'
    return 'NO'


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    print(f'#{tc} {concave(board, N)}')