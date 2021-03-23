
a, b = map(int, input().split())
que = [(b, 1)]

result = -1
while que:
    x, cnt = que.pop(0)
    if x == a:
        result = cnt
        break

    if x%2 == 0 and x/2>=a:
        que.append((x/2, cnt+1))
    elif x%10 == 1 and x//10 >= a: #elif
        que.append((x//10, cnt+1))
    else:
        break

print(result)
