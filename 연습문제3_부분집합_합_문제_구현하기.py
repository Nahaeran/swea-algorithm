def combination(n, r):
    if r == 0:
        if sum(tr) == 0:
            subset_list.append(list(tr))
    elif n < r:
        return
    else:
        tr[r - 1] = arr[n - 1]
        combination(n - 1, r - 1)
        combination(n - 1, r)


T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    subset_list = []
    for r in range(1, 11):
        tr = [0] * r
        combination(10, r)

    print(*subset_list)



# T = int(input())
#
# for tc in range(1, T + 1):
#     arr = list(map(int, input().split()))
#
#     l_idx = r_idx = 0
#     subset_list = []
#
#     while r_idx < len(arr) or l_idx < len(arr):
#         if sum(arr[l_idx:r_idx]) == 0:
#             subset_list.append(arr[l_idx:r_idx])
#             r_idx += 1
#         elif sum(arr[l_idx:r_idx]):
