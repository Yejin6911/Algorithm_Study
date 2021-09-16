import sys
INF = sys.maxsize


def solution(n, s, a, b, fares):
    answer = INF
    graph = [[INF]*n for _ in range(n)]

    for i in range(n):
        graph[i][i] = 0

    for fare in fares:
        graph[fare[0] - 1][fare[1] - 1] = fare[2]
        graph[fare[1] - 1][fare[0] - 1] = fare[2]

    # i->j로 가는 최단경로 구하기 (t를 지나서 가는 경우와 그냥 가는 경우 중 최소)
    for t in range(n):
        for i in range(n):
            for j in range(i, n):
                if i != j:
                    temp = min(graph[i][j], graph[i][t]+graph[t][j])
                    graph[i][j] = graph[j][i] = temp

    for t in range(n):
        temp = graph[s-1][t]+graph[t][b-1]+graph[t][a-1]
        answer = min(answer, temp)

    return answer
