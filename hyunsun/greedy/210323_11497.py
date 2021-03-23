
N = int(input())

for _ in range(N):
    n = int(input())
    trees = [int(x) for x in input().split()]
    trees.sort()
    maxH = 0
    for i in range(2, n):
        curH = trees[i] - trees[i - 2]
        if curH < 0:
            curH = 0-curH
        maxH = max(maxH, curH)

    print(maxH)
