from itertools import permutations
import sys

input = sys.stdin.readline

n, m = map(int, input().split()) # n : 1 ~ n까지 자연수 m : 중복없이 m개를 고름

n_list = list(range(1, n + 1)) # n_list : 1 ~ n까지 자연수로 구성된 리스트

for j in permutations(n_list, m): # permutations(iterable, r=None) : iterable에서 요소의 연속된 길이 r 순열을 반환
    print(*j)