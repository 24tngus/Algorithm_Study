import re

user_str = input()
pattern = r'(0+|[^0]+)'

split_str = re.findall(pattern, user_str)

# P_NOTE: 리스트 컴프리헨션
# item for item in split_str: 기본 리스트에서 item을 반복하여 새로운 리스트 생성을 한다.
# if '1' not in item : item을 필터 조건으로 사용한다.
zeros = [item for item in split_str if '1' not in item]
ones = [item for item in split_str if '0' not in item]

# P_NOTE: 삼항 연산자
result = len(ones) if len(zeros) > len(ones) else len(zeros)
print(result)
