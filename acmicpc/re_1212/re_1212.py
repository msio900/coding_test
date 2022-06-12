import sys

input = sys.stdin.readline

print(bin(int(input().rstrip(), 8))[2:])