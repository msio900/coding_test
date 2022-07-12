import random
# 파이썬 팀원
# l = ['민성','정화', '동윤','동훈','아연','우성','윤정','종혁','지은','현목','현주']

# 채희, 승희, 지은, 우성

# 오늘 스터디 참석자
l = ['민성','정화', '동윤','동훈','아연','우성','윤정','종혁','지은','현주']
l = random.sample(l, len(l))

# 4명당 1조로 편성
T = int(len(l)/4)
team = []
for i, name in enumerate(l):
    team.append((i%T, name))

team.sort()

for t in team:
    print(*t)