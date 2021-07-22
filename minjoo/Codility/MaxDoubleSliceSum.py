def solution(A):
    left_sum = [0] * len(A)
    right_sum = [0] * len(A)

    # 제일 처음고 마지막은 합산하지 않기 때문에 1~n-1까지만 for문을 돌게 한다.
    for i in range(1, len(A)-1):
        # 0과 비교하여 큰 값을 배열에 넣으면, 값이 작아지는 경우는 합산하지 않도록 한다.
        left_sum[i] = max(0, left_sum[i-1] + A[i])
    for i in range(len(A)-1, 0, -1):
        right_sum[i-1] = max(0, right_sum[i] + A[i-1])
    
    m = 0
    for i in range(1, len(A)-1):
        m = max(m, left_sum[i-1]+right_sum[i+1])

    return m