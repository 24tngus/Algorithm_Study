# N 만큼의 입력
#3 1 4 3 2 -> 1 2 3 3 4

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
sum_arr = []
sum_val =0

for i in range (N):
    sum_val += arr[i]
    sum_arr.append(sum_val)

print(sum(sum_arr))



