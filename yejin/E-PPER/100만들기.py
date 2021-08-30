from itertools import combinations
import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
total = sum(numbers)-100
choices = combinations(numbers, 2)

for choice in choices:
    choice = list(choice)
    if sum(choice) == total:
        for num in choice:
            numbers.remove(num)

print(*numbers)
