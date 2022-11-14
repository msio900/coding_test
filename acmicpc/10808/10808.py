import sys
from collections import Counter

S = sys.stdin.readline().strip() # 입력받은 문자열 저장
S = [str(i) for i in S] # 문자열을 리스트 자료구조로 저장

alphabet = [chr(i) for i in range(97, 123)]

X = Counter(alphabet)+Counter(S) # a-z까지 모두 1로 된 Counter의 딕셔너리 구조에 앞서 주어진 문자열의 Counter 딕셔너리 구조를 더함.
X = dict(X) # Counter 구조를 딕셔너리 구조로 변환
# 1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0
answer = []
for i in X:
    answer.append(str(X[i] - 1)) # 각각의 알파벳 값에 1을 빼서 주어진 문자열에서 알파벳당 갯수를 구함.

print(" ".join(answer))