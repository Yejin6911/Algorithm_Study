
def check(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i
    if total == number:
        return "YES"
    else:
        return "NO"


k = int(input())
numbers = list(map(int, input().split()))

results = []
for number in numbers:
    results.append(check(number))

print(results)
