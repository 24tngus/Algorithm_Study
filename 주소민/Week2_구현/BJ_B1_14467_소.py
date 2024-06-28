# 사용자 입력 값
n = int(input())

list_map = {}
for _ in range(n):
    new_list = input().split(" ")
    if new_list[0] in list_map:
        data = list_map.get(new_list[0])
        # 이전 값과 같으면 넣지 않음
        if data[-1] != new_list[1] :
            data.append(new_list[1])
    else:
        data = [new_list[1]]
        list_map[new_list[0]] = data


answer = 0
for i in list_map:
    data = list_map.get(i)
    if len(data) > 1:
        answer += len(data) - 1

print(answer)