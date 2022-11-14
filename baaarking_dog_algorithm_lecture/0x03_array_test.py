# 배열 임의의 위치에 있는 원소를 추가
def insert(idx : int, num : int, arr : list):
    arr += [0]
    for i in reversed(range(idx, len(arr))):
        arr[i] = arr[i-1]
    arr[idx] = num
    return arr
# 배열 임의의 위치에 있는 원소를 제거
def erase(idx : int, arr : list):
    for i in range(idx, len(arr)-1):
        arr[i] = arr[i+1]
    arr.pop()
    return arr

arr1 = [10, 20, 30]
print(*insert(3, 40, arr1))
# 10 20 30 40

print(*insert(1, 50, arr1))
# 10 50 20 30 40

print(*insert(0, 15, arr1))
# 15 10 50 20 30 40


arr2 = [10, 50, 40, 30, 70, 20]
print(*erase(4, arr2))
# 10 50 40 30 20

print(*erase(1, arr2))
# 10 40 30 20

print(*erase(3, arr2))
# 10 40 30