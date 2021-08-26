from itertools import combinations

numbers = list(map(int, input().split()))
combs = list(combinations(numbers, 7))

for i in range(len(combs)):
    if(sum(combs[i]) == 100):
        print(*combs[i])
        break