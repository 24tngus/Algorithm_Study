n = int(input())
n1 = 1000 - n
count = 0

list = [500, 100, 50, 10, 5, 1]
for i in list:
    count += n1 // i
    n1 %= i

print (count)