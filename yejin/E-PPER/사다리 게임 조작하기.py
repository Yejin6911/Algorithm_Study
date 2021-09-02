# 사다리가 한 개 추가될 때마다 사다리의 오른쪽과 왼쪽에 있는 번호가 서로 바뀌게 된다
# -> 사다리를 만났을 경우 두 자리가 Swap
# -> 스왑을 이용한 정렬? -> 버블 소트를 이용

# 방법1. 배열 변경하면서 실행
def solution1(goal):
    cnt = 0
    for i in range(len(goal) - 1, 0, -1):
        for j in range(i):
            if goal[j] > goal[j + 1]:
                goal[j], goal[j + 1] = goal[j + 1], goal[j]
                cnt += 1
    return cnt


# 방법2. 배열 변경 안하면서 cnt만 증가
def solution2(goal):
    cnt = 0
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if goal[j] > goal[i]:
                cnt += 1
    return cnt


n = int(input())
goal = list(map(int, input().split()))
print(solution2(goal))
