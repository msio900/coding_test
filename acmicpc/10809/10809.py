import sys
from collections import Counter

S = sys.stdin.readline().strip()
S = [str(i) for i in S]

alphabet = [chr(i) for i in range(97, 123)]

X = Counter(alphabet)+Counter(S)
X = dict(X)
# 1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0
answer = []
for i in X:
    answer.append(str(X[i] - 1))

print(" ".join(answer))