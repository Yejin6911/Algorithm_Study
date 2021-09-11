def solution(N, stages):
    answer = []
    not_clear = [0 for _ in range(N+1)]
    challenge = [0 for _ in range(N+1)]
    for stage in stages:
        if stage == N+1:
            for i in range(1, N+1):
                challenge[i] += 1
        else:
            for i in range(1, stage+1):
                challenge[i] += 1
            not_clear[stage] += 1
    rates = {}
    for i in range(1, N+1):
        if challenge[i] == 0:
            rates[i] = 0
        else:
            rates[i] = not_clear[i]/challenge[i]
    new_rates = sorted(rates.items(), key=lambda x: x[1], reverse=True)
    for rate in new_rates:
        answer.append(rate[0])
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
