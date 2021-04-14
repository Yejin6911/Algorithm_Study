import sys
input = sys.stdin.readline

r, c, k = map(int, input().rstrip().split())
data = [list(map(int, input().rstrip().split())) for _ in range(3)]


def expand():
    length = len(data)
    max_length = 0
    for i in range(length):
        temp = []
        count = {}
        for j in data[i]:
            if j != 0:
                if j in count.keys():
                    count[j] += 1
                else:
                    count[j] = 1
        s_count = sorted(count.items(), key=lambda x: (x[1], x[0]))
        for k in s_count:
            temp.append(k[0])
            temp.append(k[1])
        if len(temp) > 100:
            temp = temp[:100]
        max_length = max(max_length, len(temp))
        data[i] = temp
    for row in data:
        if len(row) < max_length:
            for _ in range(len(row), max_length):
                row.append(0)


result = 0
while True:
    if result > 100:
        result = -1
        break
    # 3X3보다 줄어들 때 고려해야함!
    if (len(data) >= r and len(data[0]) >= c) and data[r-1][c-1] == k:
        break
    else:
        if len(data) >= len(data[0]):
            expand()
        else:
            data = list(zip(*data))
            expand()
            data = list(zip(*data))
        result += 1

print(result)


# 행, 열, 따로 처리해주었을 때의 풀이
# def expand_row():
#     global now_c
#     new = []
#     max_length = now_c
#     for i in range(now_r):
#         temp = []
#         count = {}
#         for j in range(now_c):
#             if data[i][j] in count.keys():
#                 count[data[i][j]] += 1
#             else:
#                 count[data[i][j]] = 1
#         s_count = sorted(count.items(), key=lambda x: (x[1], x[0]))
#         for k in s_count:
#             if k[0] == 0:
#                 continue
#             temp.append(k[0])
#             temp.append(k[1])
#         if len(temp) > 100:
#             temp = temp[:100]
#         max_length = max(max_length, len(temp))
#         new.append(temp)
#     for i in range(len(new)):
#         if len(new[i]) < max_length:
#             for _ in range(len(new[i]), max_length):
#                 new[i].append(0)
#     now_c = max_length
#     return new


# def expand_col():
#     global now_r
#     new = []
#     max_length = now_r
#     for j in range(now_c):
#         temp = []
#         count = {}
#         for i in range(now_r):
#             if data[i][j] in count.keys():
#                 count[data[i][j]] += 1
#             else:
#                 count[data[i][j]] = 1
#         s_count = sorted(count.items(), key=lambda x: (x[1], x[0]))
#         for k in s_count:
#             if k[0] == 0:
#                 continue
#             temp.append(k[0])
#             temp.append(k[1])
#         if len(temp) > 100:
#             temp = temp[:100]
#         max_length = max(max_length, len(temp))
#         new.append(temp)
#     new_2 = [[0]*now_c for _ in range(max_length)]
#     for i in range(len(new)):
#         if len(new[i]) < max_length:
#             for _ in range(len(new[i]), max_length):
#                 new[i].append(0)
#         for j in range(len(new[i])):
#             new_2[j][i] = new[i][j]
#     now_r = max_length
#     return new_2
