T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    aj = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    
    if n>=m :
        long = aj
        short = bj
    else:
        long = bj
        short = aj

    arr = []
    for i in range(len(long)-len(short)+1):
        result=0
        for j in range(len(short)):
            result += long[i+j]*short[j]
        arr.append(result)
    print("#"+str(test_case), max(arr))