def solution(A):
    maxnum = max(A)
    if(maxnum >= 0):
        visited = [0] * (maxnum+1)
        for i in range(len(A)):
            if(A[i]-1 >= 0):
                visited[A[i]-1] = 1
        return visited.index(0)+1

    else:
        return 1