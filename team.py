import random
# 파이썬 팀원
# l = ['정화', '우성', '동윤', '민성', '민희', '동훈', '아연', '민진', '청하', '주희', '좌홍']

# 채희, 승희, 지은, 우성

# 오늘 스터디 참석자
l = ['정화', '우성', '동윤', '민성', '민희', '동훈', '아연', '민진', '좌홍']
l = random.sample(l, len(l))

# 4명당 1조로 편성
T = int(len(l)/4)
team = []
for i, name in enumerate(l):
    team.append((i%T, name))

team.sort()

for t in team:
    print(*t)