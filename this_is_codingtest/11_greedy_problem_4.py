import sys

N = int(sys.stdin.readline())

coins = sys.stdin.readline().split()
# 3 2 1 1 9
coins = [int(i) for i in coins]

print(coins)
coins.sort()
print(coins)

stack = []
for i in range(len(coins)):
 for j in range(i+1, len(coins)+1):
  stack.append(sum(coins[i:j]))
print(list(set(stack)))

not_list = [i for i in range(1, max(stack))]
print(not_list)

for i in stack:
 if i in not_list:
  not_list.remove(i)

not_list.sort()

print(not_list[0])