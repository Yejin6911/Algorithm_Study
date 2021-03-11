n = int(input())
rope = []

for _ in range(n):
    rope.append(int(input()))

weight = 0
count = 1
rope.sort(reverse=True) # 역순으로 정렬

for i in range(n):
    minimum = rope[count-1]
    temp = minimum*count
    if(temp > weight):
        weight = temp
    count += 1

print(weight)