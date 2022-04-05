import sys

input = sys.stdin.readline

n = int(input())
member = list(map(int, input().split()))
member.sort()

result = 0 # 총 그룹의 수

count = 0 # 현재 그룹에 포함된 모험가의 수

for i in member: # 공포도를 낮은 것부터 하나씩 확인하며
 count +=1 # 현재 그룹에서 해당 모험가를 포함시키기
 if count >= i : # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹을 결성함.
  result += 1 # 총 그룹의 수 증가시키기
  count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력
