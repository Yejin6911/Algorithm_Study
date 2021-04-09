from itertools import combinations

n, m = map(int,input().split())
citys = [ list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if citys[i][j] == 1:
            houses.append((i,j))
        elif citys[i][j] == 2:
            chickens.append((i,j))

mindist = 100000 #최소값 구하기 위함 #모든 치킨 조합의 총 거리 중에 최소
for possible_chickens in list(combinations(chickens, m)):
    curdist = 0 #현재 치킨 조합일때 총 거리
    for house in houses:
        chickendist = 100000 #최소값 구하기 위함
        for chicken in possible_chickens:
            chickendist = min(chickendist, abs(chicken[0]-house[0]) + abs(chicken[1]-house[1]))
        curdist += chickendist
        if curdist >= mindist: break #각 치킨 거리 더하고 있는데, 이미 이전까지 중의 최소 치킨 거리보다 크면, 여기서 얘는 더 이상 구하기 않고 끝내기
    mindist = min(mindist, curdist)

print(mindist)
             
