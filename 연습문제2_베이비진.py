def is_win(arr, i, N):
    if i == N:
        if is_baby_gin(p):
            result.append(True)
    else:
        for j in range(N):
            if not used[j]:
                p[i] = arr[j]
                used[j] = 1
                is_win(arr, i+1, N)
                used[j] = 0


def is_baby_gin(arr):
    if arr[0] == arr[1] == arr[2]:
        if arr[3] == arr[4] == arr[5]:
            return True
        elif arr[4] == arr[3] + 1 == arr[5] - 1:
            return True
    elif arr[1] == arr[0] + 1 == arr[2] - 1:
        if arr[3] == arr[4] == arr[5]:
            return True
        elif arr[4] == arr[3] + 1 == arr[5] - 1:
            return True
    return False


T = int(input().strip())

for tc in range(1, T + 1):
    cards = list(map(int, input().strip()))
    p = [0] * 6
    used = [0] * 6
    result = []
    is_win(cards, 0, 6)
    if True in result:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
