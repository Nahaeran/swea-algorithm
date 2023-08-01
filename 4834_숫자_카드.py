T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input()))

    card = li[0]
    num_of_card = li.count(card)
    for e in li:
        if num_of_card <= li.count(e):
            if card < e:
                card = e
            num_of_card = li.count(card)
    print(f'#{tc} {card} {num_of_card}')