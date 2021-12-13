import sys

input = sys.stdin.readline().split()

N = int(input[0])
K = int(input[1])

array = list(range(1,N+1))
num_array = [i*K-1 for i in range(1, N+1)]


out_array = []

print(array)
print(num_array)
j = 0
for i in num_array:
    print("조건문 전")
    print(array)
    print(out_array)
    if len(array) <= i-j:
        print("넘어감")
        array = array + array
        out_array.append(array.pop(i-j))
        print(array)
        print(out_array)
    else:
        print("안 넘어감")
        out_array.append(array.pop(i-j))
        print(array)
        print(out_array)
    j += 1
# [1, 2, 3, 4, 5, 6, 7]   3번째 [2] 3 탈락 < 3 >
# [1, 2, 4, 5, 6, 7]      3번째 [5] 6 탈락 < 3, 6 >
# [1, 2, 4, 5, 7]         3번째 [1] 2 탈락 < 3, 6, 2 >
# [1, 4, 5, 7]            3번째 [4] 7 탈락 < 3, 6, 2, 7 >

