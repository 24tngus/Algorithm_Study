# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔

# 입력: 금액
N = 1000 -int(input())
money = [500,100,50,10,5,1]
ans = 0

for i in money:
    ans += N//i #제일 큰 코인 수로 갯수 넣기
    N = N%i     #제일 큰 코인수 빼서 넣기

print(ans)