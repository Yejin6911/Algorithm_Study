import sys
input = sys.stdin.readline

n, length = map(int, input().split())
board = list(map(int, input().split()) for _ in range(n))

def check(arr):
    cnt = 0
    flag = 0
    for i in range(n):
        if(i == 0):
            h = arr[i]
            continue
        
        if(flag and cnt):
            

        if(h != arr[i]):
            if(abs(h - arr[i]) == 1):
                cnt = length - 1
                flag = arr[i]
            else:
                return 0
