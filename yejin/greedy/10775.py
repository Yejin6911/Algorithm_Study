import sys

G = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())

gates = [0 for _ in range(G+1)]
data = []
for i in range(P):
    data.append(int(sys.stdin.readline().rstrip()))

result = 0

# 시간초과
# def find(gate):
#     for i in range(gate, 0, -1):
#         if gates[i] == 0:
#             return i
#     return 0

# for i in range(P):
#     if next > 0:
#         gates[next] = i+1
#         result += 1
#     else:
#         break
# print(result)

# union find 방법 사용 - 방법 기억하기!!!
parent = {i: i for i in range(G+1)}


def find_parent(index):
    if index == parent[index]:
        return index
    else:
        p = find_parent(parent[index])
        parent[index] = p
        return parent[index]


def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    parent[x] = y


for i in data:
    x = find_parent(i)
    if x == 0:
        break
    result += 1
    union(x, x-1)

print(result)
