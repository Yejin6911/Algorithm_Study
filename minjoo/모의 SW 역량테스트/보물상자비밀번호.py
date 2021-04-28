import sys
from collections import deque
input = sys.stdin.readline

sixteen = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split()) # 숫자의 개수, 크기 순서
    nums = deque(input().strip()) # 16진수 숫자
    length = n//4
    candidates = []
    temp = ''
    for _ in range(length+1):
        nums.rotate(1)
        for i in range(n):
            if (len(temp) < length):
                temp += nums[i]
            else:
                temp = ''.join(temp)
                candidates.append(temp)
                temp = nums[i]

    candidates = list(set(candidates))
    candidates.sort(reverse = True)
    # print(candidates)

    result = 0
    num = candidates[k-1]
    # print(num)
    for i in range(length):
        result += (sixteen.index(num[length-i-1]) * (16 ** i))

    print("#{0} {1}".format(tc, result))
