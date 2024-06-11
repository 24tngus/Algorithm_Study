'''
@ no. 11399 - ATM
'''

# n = 5
# wait_list = [3, 1, 4, 3, 2] # 1 ~ 5번까지의 사람들 atm 사용시간

n = int(input())

wait_list = list(map(int, input().split(' ')))
wait_list.sort()
result = []
for i in range(len(wait_list)):

    p = sum(wait_list[:i+1])
    result.append(p)

print(sum(result))