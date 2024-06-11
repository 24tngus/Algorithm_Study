data = list(map(int, input()))

N = -1
result = 0

for i in data:
    if (i != N):
        N = i
        result += 1
    
print(result//2)