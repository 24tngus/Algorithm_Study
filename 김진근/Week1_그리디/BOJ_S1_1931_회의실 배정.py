# N만큼의 회의실
# 뒤에 끝나는 시간을 기준으로 정렬하고, 순서대로 돌면서 확인하기
# 배열값을 배열로 입력받기

n = int(input())
room = []

for i in range(n):
    start, end = map(int,input().split())
    room.append([start, end])

room.sort(key=lambda x:(x[1],x[0])) # 끝나는 시간, 시작시간으로 정ㄹ

ans = 1 # 무조건 회의는 1번은 시행
end_time = room[0][1] # 첫번째 끝나는 시간

#전체 돌면서 (첫번째 선택한것 제외) 끝나는 시간과 시작시간 비교하고
# 조건에 충족하면 end_time 에는 끝나는 시간 넣기
for i in range(1,n):
    if room[i][0] >= end_time:
        ans += 1
        end_time = room[i][1]

print(ans)