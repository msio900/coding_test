import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    doc = list(map(int, input().split()))
    dict = dict