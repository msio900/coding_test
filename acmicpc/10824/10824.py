import sys

# .split()
# .rstrip()
# list(map(str, ....))

A, B, C, D = sys.stdin.readline().split()   # input()

print(int(A+B)+int(C+D))