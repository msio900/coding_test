import sys

S = list(map(str, sys.stdin.readline().strip()))

alphabet = []

for i in range(ord('a'), ord('z')+1):
    for j in range(len(S)):
        if S[j] == chr(i):
            print(f'{chr(i)}는 {j}번째,  {S[j]} 등장 ')
            alphabet.append(j)
            break
        else:
            alphabet.append(-1)
print(alphabet)