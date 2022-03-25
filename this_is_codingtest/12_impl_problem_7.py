import sys

# 특정 점수에 도달했을 때 사용할 수 있는 기술'럭키스트레이트'
# 현재 캐릭터 점수 = N
# 자릿수 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿 수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황
# 123402
# 1+2+3 = 6
# 4+0+2 = 6

N = str(sys.stdin.readline().rstrip())

if sum(list(map(int,N[:len(N)//2]))) == sum(map(int,list(N[len(N)//2:]))):
    print("LUCKY")
else:
    print("READY")

