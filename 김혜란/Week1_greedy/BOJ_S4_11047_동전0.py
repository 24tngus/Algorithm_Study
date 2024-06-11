'''
@ no. 11047 - 동전 0
'''

n, k = map(int, input().split(' '))
# n, k = map(int, '10 4200'.split(' '))

# 동전의 종류를 동전의 개수 n만큼 입력 받음
coin_list = []
for _ in range(n):
    coin_list.append(int(input()))

# coin_list = [1, 5,10,50,100,500,1000,5000,10000, 50000]
coin_list.sort(reverse=True)

cnt = 0
for coin in coin_list:
    if k / coin >= 1:

        cash_cnt = k // coin
        k -= coin * cash_cnt
        cnt += cash_cnt

print(cnt)



'''
10 4790
1
5
10
50
100
500
1000
5000
10000
50000'''