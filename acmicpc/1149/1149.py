import sys

input = sys.stdin.readline

str_arr = input()
bomb = input()
while bomb in str_arr:
    print(str_arr, f'{bomb}')
    str_arr = str_arr.strip(bomb)
    print(str_arr)