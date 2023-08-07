# sorted 내장함수 사용
# T = int(input())
#
# priority_dict = {
#     "ZRO" : 0,
#     "ONE" : 1,
#     "TWO" : 2,
#     "THR" : 3,
#     "FOR" : 4,
#     "FIV" : 5,
#     "SIX" : 6,
#     "SVN" : 7,
#     "EGT" : 8,
#     "NIN" : 9
# }
#
# for tc in range(1, T+1):
#     tc, N = input().split()
#     N = int(N)
#     li = list(input().split())
#
#     sorted_li = sorted(li, key=lambda x: priority_dict[x])
#     print(f'{tc}')
#     print(*sorted_li)

T = int(input())
priority_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    tc, N = input().split()
    N = int(N)
    li = list(input().split())

    result = []
    for string in priority_list:
        for e in li:
            if e == string:
                result.append(e)
    print(tc)
    print(*result)