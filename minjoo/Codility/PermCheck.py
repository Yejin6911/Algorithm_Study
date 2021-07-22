def solution(A):
    maxcnt = max(A) # 4
    if(len(A) < maxcnt):
        return 0
    cnt = 0
    visited = [0] * (maxcnt + 1)
    for i in range(len(A)):
        if(visited[A[i]] == 0):
            visited[A[i]] = 1
            cnt += 1
        else:
            return 0
    if(cnt == maxcnt):
        return 1
    else:
        return 0