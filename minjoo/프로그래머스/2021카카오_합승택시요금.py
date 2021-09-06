import sys
answer = sys.maxsize
m = sys.maxsize

def solution(n, s, a, b, fares):

    f = [[] for _ in range(n+1)]
    for i in range(len(fares)):
        x, y, m = fares[i]
        f[x].append([y, m])
        f[y].append([x, m])
    # print(f)
    # print()
    dfs(s, s, a, b, f, 0, [s])

    print(answer)
    

# 개별적인 dfs
def small_dfs(start, end, v, money, f):
    global m
    if(start == end):
        m = min(m, money)
        return

    for i in range(len(f[start])):
        if(f[start][i][0] not in v):
            small_dfs(f[start][i][0], end, v+[f[start][i][0]], money+f[start][i][1], f)

# a와 b가 같이가는 dfs
def dfs(a_s, b_s, a, b, f, money, visited):
    global answer, m
    
    if(a_s == a): # a 도착
        small_dfs(b_s, b, [b_s], 0, f) # b의 dfs
        b_money = m
        m = sys.maxsize
        temp_money = money + b_money
        answer = min(answer, temp_money)
        

    if(b_s == b): # b 도착
        small_dfs(a_s, a, [a_s], 0, f) # a의 dfs
        a_money = m
        m = sys.maxsize
        temp_money = money + a_money
        answer = min(answer, temp_money)
        

    small_dfs(a_s, a, [a_s], 0, f) # a의 dfs
    a_money = m
    m = sys.maxsize

    small_dfs(b_s, b, [b_s], 0, f) # b의 dfs
    b_money = m
    m = sys.maxsize

    # print(a_money, b_money, money, visited)
    temp_money = a_money + b_money + money
    answer = min(answer, temp_money)

    for i in range(len(f[a_s])):
        if(f[a_s][i][0] not in visited):
            nv = visited + [f[a_s][i][0]]
            nm = money + f[a_s][i][1]
            dfs(f[a_s][i][0], f[a_s][i][0], a, b, f, nm, nv)
            


# n = 6
# s = 4
# a = 6
# b = 2
# fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# solution(n, s, a, b, fares)

# n = 7
# s = 3
# a = 4
# b = 1
# fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
# solution(n, s, a, b, fares)

# n = 6
# s = 4
# a = 5
# b = 6
# fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
# solution(n, s, a, b, fares)