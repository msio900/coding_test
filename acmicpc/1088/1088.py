import sys

# in[0]
# 2
# 1 3
# 1
# out[0]
# 0.5

N = int(sys.stdin.readline())
cake_gram = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
print(cake_gram)
for _ in range(M):
    cake_gram.sort(reverse=True)
    cake_gram.append(cake_gram.pop()/2)