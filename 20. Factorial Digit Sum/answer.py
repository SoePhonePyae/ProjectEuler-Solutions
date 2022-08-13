def factorial(num):
    if num == 1:
        return 1

    return num * factorial(num - 1)

big = factorial(100)
total = 0

for i in str(big):
    total += int(i)

print(total)
