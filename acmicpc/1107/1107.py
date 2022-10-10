# import sys
#
# input = sys.stdin.readline
#
# nums = [str(i) for i in range(10)]
#
# # print(nums)
# n = input()
# m = input()
# broken_buttons = list(input().split())
#
# for button in broken_buttons:
#     nums.remove(button)
# # print(nums)
# answer = 0
# if 98 <= int(n) <= 103:
#     print(abs(100 - int(n)))
# else:
#     target_list = list(n)[:-1]
#     for num in target_list:
#         if num in nums:
#             answer +=1
#         else:
#             print(num)
#

min_cnt = 0x3f3f3f3f
num_int = 0
btn_set = {i for i in range(0, 10)}


def find(num):
    global min_cnt, num_int, btn_set

    for btn in btn_set:
        tmp_num = num + str(btn)
        min_cnt = min(min_cnt, abs(num_int - int(tmp_num)) + len(tmp_num))

        if len(tmp_num) < 6:
            find(tmp_num)


def main():
    global min_cnt, num_int, btn_set

    num_int = int(input())
    n = int(input())

    min_cnt = min(min_cnt, abs(100 - num_int))
    btn_set -= set(map(int, input().split(' '))) if n else set()

    find('') if n < 10 else ''
    print(min_cnt)


main()
