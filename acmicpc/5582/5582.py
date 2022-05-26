import sys
input = sys.stdin.readline

S1 = input().rstrip()
S2 = input().rstrip()
answer = 0

dp = [[0]*(len(S2)+1) for _ in range(len(S1)+1)]

for i in range(1, len(S1)+1):
    for j in range(1, len(S2) + 1):
        if (S1[i-1] == S2[j-1]):
            dp[i][j] = dp[i-1][j-1]+1
            answer = max(dp[i][j], answer)
print(answer)
