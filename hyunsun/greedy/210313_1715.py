N = int(input())
cards = [int(input()) for i in range(N)]

cards.sort()
current = cards[0]
sum = 0


for i in range(1,N):
    current += cards[i]
    sum += current


print(sum)
