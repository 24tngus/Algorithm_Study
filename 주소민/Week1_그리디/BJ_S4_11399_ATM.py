# 사용자 입력 값
people = int(input())
time_list = list(map(int, input().split()))
time_list.sort()

answer_list = []
for i in range(people):
    if i == 0:
        answer_list.append(time_list[i])
        continue

    # P_NOTE: [리스트] 인덱스 슬라이싱, 배열 값 더하기
    prev_time = sum(time_list[0:i])
    answer_list.append(prev_time + time_list[i])

print(sum(answer_list))
