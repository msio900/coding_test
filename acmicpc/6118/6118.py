import sys
import string

input = sys.stdin.readline

num = oct(int(input(), 2))[2:] #.rstrip()
# to_ten = 0
# for i, k in enumerate(num):
#     # print((len(num) - i - 1), int(k))
#     to_ten += 2**(len(num) - i - 1) * int(k)
#
# answer = ''
# while to_ten != 0:
#     answer += str(to_ten % 8)
#     to_ten //= 8
#
# print(answer[::-1])


print(num)