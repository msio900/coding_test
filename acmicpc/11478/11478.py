import sys

input = sys.stdin.readline

S = input().rstrip()
ans = []
for i in range(len(S)+1):
    for j in range(i + 1, len(S)+1):
        print(S[i:j])
        ans.append(S[i:j])
print(len(set(ans)))