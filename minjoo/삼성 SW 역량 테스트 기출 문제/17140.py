import sys
input = sys.stdin.readline
from copy import deepcopy

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

def solution(board):
    for sec in range(101): # 100초 동안
        if(r-1<len(board) and c-1<len(board[0])): # 범위체크
            if(board[r-1][c-1] == k):
                return sec # 몇초 걸렸는지 반환

        if(len(board) >= len(board[0])): # R연산
            board = op(board) # 연산 수행
            board = size(board) # 0 채워주기
        else: # C 연산
            tempboard = turn(board) # 열 -> 행
            tempboard = op(tempboard) # 연산 수행
            tempboard = size(tempboard) # 0 채워주기
            board = turn(tempboard) # 다시 행 -> 열
            
    return -1 # 100초 이내에 불가능
 
def turn(board): # 열 -> 행 OR 행 -> 열
    tempboard = [[] for _ in range(len(board[0]))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            tempboard[j].append(board[i][j])
    return tempboard

def op(board): # 연산 수행
    for i in range(len(board)):
        hang = board[i]
        board[i] = []
        hangset = list(set(hang)) # 숫자 종류
        if(0 in hangset): # 0은 안 셈
            hangset.remove(0)
        temp = []
        for j in range(len(hangset)):
            temp.append([hangset[j], hang.count(hangset[j])]) # [숫자, 나온횟수]
        temp.sort(key=lambda x:(x[1], x[0]))
        for a in range(len(temp)):
            board[i] += temp[a]
    return board

def size(board): # 0 채워주기
    max_length = 0
    for hang in board:
        if(max_length < len(hang)):
            max_length = len(hang)
    for i in range(len(board)):
        while(len(board[i]) != max_length):
            board[i].append(0) # 0 채워주기
    return board
    
print(solution(board))