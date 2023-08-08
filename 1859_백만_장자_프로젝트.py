# def calculate_profit(N, li):
#     profit = 0
#     sell_point = [-1]
#
#     for i in range(N):
#         max_sell_point = li[i]
#         for j in range(i, N):
#             if max_sell_point < li[j]:
#                 max_sell_point = li[j]
#         idx = li.index(max_sell_point)
#         if idx not in sell_point:
#             sell_point.append(idx)
#
#     if sell_point == [-1]:
#         sell_point.append(N - 1)
#     elif li[-1] > li[-2]:
#         sell_point.append(N - 1)
#     elif len(sell_point) == N:
#         return 0
#     # print(sell_point)
#     for point_idx in range(1, len(sell_point)):
#         for i in range(sell_point[point_idx - 1] + 1, sell_point[point_idx]):
#             profit += li[sell_point[point_idx]] - li[i]
#     return profit
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     li = list(map(int, input().split()))
#
#     profit = calculate_profit(N, li)
#     print(f'#{tc} {profit}')

# 9
# 5 23 2 4 8 6 5 4 6

for tc in range(1, int(input()) + 1):
    N = int(input())
    li = list(map(int, input().split()))
    profit = 0
    max_price = li[N - 1]

    for i in range(N - 2, -1, -1):
        if li[i] > max_price:
            max_price = li[i]
        else:
            profit += max_price - li[i]

    print(f'#{tc} {profit}')