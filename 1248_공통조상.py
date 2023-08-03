# {자식노드 : 부모노드} 형식으로 dict 생성
def makeDict(edges):
    resultDict = {1: 0}
    for i in range(len(edges)):
        resultDict[edges[i][0]] = edges[i][1]
    return resultDict


# 공통조상 찾기
def findCommon(resultDict, v1, v2):
    v1Parents = []
    v2Parents = []
    tempV1 = v1
    tempV2 = v2
    while tempV1 != 1:
        tempV1 = resultDict[tempV1]
        v1Parents.append(tempV1)
    while tempV2 != 1:
        tempV2 = resultDict[tempV2]
        v2Parents.append(tempV2)
    common = [x for x in v1Parents if x in v2Parents]
    return common[0]


# 서브트리의 크기 구하기
def sizeOfSubTree(resultDict, root):
    nextRoot = []
    total = 0
    for k, v in resultDict.items():
        if v == root:
            total += 1
            nextRoot.append(k)
    for tempRoot in nextRoot:
        total += sizeOfSubTree(resultDict, tempRoot)
    return total

T = int(input())
for tc in range(1, T + 1):
    numV, numE, v1, v2 = map(int, input().split())
    li = list(map(int, input().split()))
    edges = []

    for i in range(0, len(li), 2):
        edges.append([li[i + 1], li[i]])
    edges.sort()

    resultDict = makeDict(edges)
    common = findCommon(resultDict, v1, v2)
    nodes = sizeOfSubTree(resultDict, common) + 1
    print(f'#{tc} {common} {nodes}')