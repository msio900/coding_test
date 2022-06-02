import random
# 파이썬 팀원
# l = ["동윤", "민성", "민진", "민희", "정화", "좌홍", "주희", "청하"]

# 채희, 승희, 지은, 우성

# 오늘 스터디 참석자
l = ["동윤", "민성", "민진", "민희", "정화", "좌홍", "주희", "청하"]
l = random.sample(l, len(l))

# 4명당 1조로 편성
T = int(len(l)/4)
team = []
for i, name in enumerate(l):
    team.append((i%T, name))

team.sort()

for t in team:
    print(*t)