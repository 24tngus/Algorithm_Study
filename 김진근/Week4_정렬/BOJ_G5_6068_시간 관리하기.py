import sys
input = sys.stdin.readline # 빠른 입력
print = sys.stdout.write # 빠른 출력, 출력은 반드시 문자열로

"""
4
3   5
8   14
5   20
1   16
->
5   20
1   16
8   14
3   5
-> 20 19 18 17 16
-> 15
-> 14 13 12 11 10 9 8 7 
-> (6) 4 3 2 => 2초부터 시작
"""
N = int(input())
arr = []
for i in range(N):
    #T_i 완성될때 필요한 시간, S_i끝내야하는 시간
    tmp = list(map(int, input().split()))
    arr.append(tmp)

#끝내야하는 시간 기준으로 뒤에서 부터 정렬
sort_arr = sorted(arr,key=lambda x:x[1], reverse=True)

now = sort_arr[0][1] #마지막 시간

for i in range(N):

    # 쭉 연결
    if sort_arr[i][1] <= now:
        now = (sort_arr[i][1] - sort_arr[i][0])
    #중간에 끊어져있을때
    else:
        now -= sort_arr[i][0]

if now >= 0:
    print(str(now))
else:
    print(str(-1))