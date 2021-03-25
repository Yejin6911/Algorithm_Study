from copy import deepcopy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def rotate(n, b): # 오른쪽 90도 회전
    new_b = deepcopy(b)
    for i in range(n):
        for j in range(n):
            new_b[j][n-i-1] = b[i][j]
    return new_b

def convert(n, b):
    new_lst = [i for i in b if i!=0] # 0을 제외한 list 저장
    for i in range(1, len(new_lst)):
        if(new_lst[i-1] == newlist[i]):
            new_lst[i-1] *= 2
            new_lst[i] = 0
    new_lst = [i for i in new_lst if i!=0]
    return new_lst + [0]*(n-len(new_lst)) # list길이만큼 오른쪽에 0추가

def dfs(n, b, count):
    result = max([max(i) for i in b]) # 최댓값
    if(count == 0):
        return result
    
    for _ in range(4):
        c = [convert(n, i) for i in b] # list 한줄씩 변환한뒤 합침
        result = max(result, dfs(n, c, count-1))
        b = rotate(n, b)
    return result

print(dfs(n, board, 5))