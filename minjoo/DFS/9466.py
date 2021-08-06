import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    global result
    visited[x] = 1
    cycle.append(x) # 사이클을 이루는 팀을 확인하기 위함
    number = numbers[x] # 다음 방문 장소

    if(visited[number]): # 방문했다면
        if(number in cycle):
            result += cycle[cycle.index(number):] # 사이클이 되는 구간 부터만 팀을 이룸
        return
    else:
        dfs(number)

for _ in range(int(input())):
    n = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [1] + [0]*n # 방문여부 확인용
    result = []

    for i in range(1, n+1):
        if(not visited[i]): # 방문하지 않았다면
            cycle = []
            dfs(i)
            
    print(n - len(result)) # 팀에 없는 사람 수