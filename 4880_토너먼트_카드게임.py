def play_rsp(i, j):
    if (cards[j] == 1 and cards[i] == 3) or \
            (cards[j] == 2 and cards[i] == 1) or \
            (cards[j] == 3 and cards[i] == 2):
        return j
    else:
        return i


def find_winner(cards, i, j):
    if i >= j:
        return play_rsp(i, j)
    else:
        left = find_winner(cards, i, (i + j) // 2)
        right = find_winner(cards, (i + j) // 2 + 1, j)
        return play_rsp(left, right)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))

    print(f'#{tc} {find_winner(cards, 0, N-1) + 1}')