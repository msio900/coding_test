import sys
import math
from functools import reduce
# 10! = 10*9*8*...*1

answer = 0
N = int(sys.stdin.readline())

for i in reversed(str(math.factorial(N))):
    if i == '0':
        answer += 1
    else:
        break

print(answer)


