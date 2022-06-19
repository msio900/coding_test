# import sys
#
# A, B = map(int, sys.stdin.readline().split())
# m = int(sys.stdin.readline())
# # print(A, B)
# # print(m)
#
# A_nums = list(map(int, sys.stdin.readline().split()))
#
# # print(A_nums)
# A_num = 0
# # 10진법으로 변환
# for i in range(m):
#     A_num += A_nums[i]*A**((m-1)-i)
#
# B_nums = []
# while A_num != 0:
#     B_nums.append(str(A_num % B))
#     A_num = A_num // B
#
# print(' '.join(B_nums[::-1]))


for i in range(2, 10):
    print(i)