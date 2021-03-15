n, m = map(int, input().split())  # 세로, 가로
if n == 1:
    print(1)
elif n == 2: # 가로로 2칸씩 몇 번 이동할 수 있는지
    print(min(4, (m + 1) // 2))
else:
    if m <= 6:
        print(min(4, m)) # 최대로 이동하기 위해서는 오른쪽으로 한칸씩 이동
    else:
        print(m - 2) # 2 + (m-5) + 1
         # 2: 2,3번 이동 1회씩 / m-5: 오른쪽으로 이동 