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
    for i in range(len(arr) - 2):
        if arr[i + 1] == arr[i] + 1 == arr[i + 2] - 1:
            return True
        if arr[i] == arr[i + 1] == arr[i + 2]:
            return True
    return False


T = int(input())

for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    a_card = [cards[0], cards[2]]
    b_card = [cards[1], cards[3]]
    i = 4
    win = ''

    while i < 12:
        if i % 2:
            b_card.append(cards[i])
            p = [0] * len(b_card)
            used = [0] * len(b_card)
            result = []
            is_win(b_card, 0, len(b_card))
            if True in result:
                win = 'b'
                break
        else:
            a_card.append(cards[i])
            p = [0] * len(a_card)
            used = [0] * len(a_card)
            result = []
            is_win(a_card, 0, len(a_card))
            if True in result:
                win = 'a'
                break
        i += 1

    if win == 'a':
        print(f'#{tc} 1')
    elif win == 'b':
        print(f'#{tc} 2')
    elif win == '':
        print(f'#{tc} 0')
