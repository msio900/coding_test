import sys

N = int(sys.stdin.readline())

# -13   = -2 * (7)  +1
# 7     = -2 * (-3) +1
# -3    = -2 * (2)  +1
# 2     = -2 * (-1) +0
# -1    = -2 * (1)  +1
# 1     = -2 * (0)  +1

if not N:
    sys.stdout.write('0')
    exit()
res = ''
while N:
    if N%(-2):
        res = '1' + res
        N = N//-2 + 1
    else:
        res = '0' + res
        N = N//-2
print(res)