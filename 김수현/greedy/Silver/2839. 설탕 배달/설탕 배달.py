n = int(input())

result = 0

while n > 0:
    if (n % 5 == 0):
        n -= 5
        result += 1
    elif (n % 3 == 0):
        n -= 3
        result += 1
    elif (n > 5):
        n -= 5
        result += 1
    else:
        result = -1
        break

print(result)