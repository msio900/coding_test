import sys

input = sys.stdin.readline

change = 0
prev = '?'
string = input().rstrip()
for i in string:
    if i != prev: change += 1
    prev = i
print(change//2)