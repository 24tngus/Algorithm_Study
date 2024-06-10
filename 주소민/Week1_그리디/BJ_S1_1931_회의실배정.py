# 사용자 입력 값
max_room = int(input())

reserve_list = list()
for _ in range(max_room):
    start, end = map(int, input().split())
    if _ <= max_room:
        reserve_list.append([start, end])

# P_NOTE: sorted, 람다 사용
sorted_list = sorted(reserve_list, key=lambda x: (x[1], x[0]))

answer = 1
pointer = 0
for i in range(max_room - 1):
    next_pointer = i + 1
    now_reserve = sorted_list[pointer]
    next_reserve = sorted_list[next_pointer]

    if now_reserve[1] <= next_reserve[0]:
        # 포인터 이동
        pointer = next_pointer
        answer += 1

# NOTE: 단순 STACK으로 배정된 방을 저장하고 확인하는 식으로 진행하였지만 실패.
print(answer)