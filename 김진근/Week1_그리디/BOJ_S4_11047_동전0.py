# N,K 입력
# N만큼의 동전 종류로 최소한의 동전을 사용해서 K 만들어라
N,K = map(int,input().split())
type_arr = []
cnt =0
for i in range(N):
    type_arr.append(int(input()))

type_arr.sort(reverse=True) #내림차순 정렬

for j in type_arr:
    if j>K:
        continue
    else:
        cnt+= K//j
        K=K%j

print(cnt)

