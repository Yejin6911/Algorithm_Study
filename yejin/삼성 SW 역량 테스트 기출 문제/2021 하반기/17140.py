import sys
input = sys.stdin.readline


def calculate():
    max_len = 0
    len_A = len(A)
    for x in range(len_A):
        count = {}
        for y in range(len(A[x])):
            if A[x][y] != 0:
                if A[x][y] in count.keys():
                    count[A[x][y]] += 1
                else:
                    count[A[x][y]] = 1
        count = sorted(count.items(), key=lambda x: (x[1], x[0]))
        new = []
        for a, b in count:
            new.extend([a, b])
        if len(new) > 100:
            new = new[:100]
        max_len = max(max_len, len(new))
        A[x] = new
    for x in range(len(A)):
        if len(A[x]) < max_len:
            A[x].extend([0]*(max_len-len(A[x])))


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

t = 0
while True:
    if t > 100:
        print(-1)
        break
    # r,c보다 A의 열, 행 길이가 짧아질 때 고려
    if len(A) >= r and len(A[0]) >= c and A[r-1][c-1] == k:
        print(t)
        break
    # R연산
    if len(A) >= len(A[0]):
        calculate()
    # C연산
    else:
        A = list(map(list, zip(*A)))
        calculate()
        A = list(map(list, zip(*A)))
    t += 1
