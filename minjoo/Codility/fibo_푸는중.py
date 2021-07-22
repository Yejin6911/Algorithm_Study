# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def fibo(n):
    nums = [0, 1]
    while(nums[-1] < n):
        nums.append(nums[-1] + nums[-2])
    return nums

def solution(A):
    if(len(A) == 0):
        return -1
    
    nums = fibo(len(A) + 2)
   
    jump = 0
    idx = -1 # 개구리의 현재 위치
    next = 0
    while(idx < len(A) and next < len(A)):
        if(A[next] == 0):
            next += 1
            continue
        else: # 나뭇잎 있음
            dis = next - idx # 거리 계산
            if(dis in nums):
                idx = next
                jump += 1
                next += 1
            else:
                continue
    
    if((next - idx) in nums):
        jump += 1
        return jump
    else:
        return -1
