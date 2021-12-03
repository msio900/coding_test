import sys

T = int(sys.stdin.readline())

for _ in range(T):
    ps = sys.stdin.readline().rstrip()
    for i in range(len(ps)-1):
        if ps[i] == '(':
            for j in range(i+1, len(ps)-1):
                if ps[j] == ')':
                    pass
                if ps[j] == 

