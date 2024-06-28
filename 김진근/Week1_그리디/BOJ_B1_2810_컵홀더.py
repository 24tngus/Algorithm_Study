

n = int(input()) #좌석수
member = input() #좌석정보
ans = 0
cnt = member.count('LL') #커플석 -> 한쌍

# 컵홀더 위치
# 양끝
# 커플석 사이는 컵홀더 X
# 컵홀더에 꽂을수 있는 최대 사람의수
# 좌석사이 1개씩
if (cnt <= 1): #커플석이 1쌍 미만
   ans = len(member) #커플석이 1쌍 미만이면 그냥 모든사람이 꽂을수 있다

else:
   ans = len(member)+1-cnt # 커플석 만큼 뺴고 한자리 더하기

print(ans)