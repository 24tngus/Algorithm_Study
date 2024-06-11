n = int(input())

data = []
dic = {}

for _ in range(n):
    data.append(input())
 
for d in data:
    for i in range(len(d)):
        if d[i] in dic:
            dic[d[i]] += 10 ** (len(d)-i-1)
        else:
            dic[d[i]] = 10 ** (len(d)-i-1)

dic = list(dic.values())
dic.sort(reverse=True)

result = 0
i = 0
for n in range(9, 9-len(dic), -1):
    result += dic[i] * n
    i += 1

print(result)