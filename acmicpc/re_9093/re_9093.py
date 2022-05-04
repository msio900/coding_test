import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    sentence = input().rstrip().split(' ')
    for i in range(len(sentence)):
        print(sentence[i][::-1], end=' ')
    print()

