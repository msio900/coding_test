def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[0])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)
    return answer

if __name__ == '__main__':
    arr1, arr2 = [[1,2],[2,3]], [[3,4],[5,6]]
    print(solution(arr1, arr2))
    arr1, arr2 = [[1],[2]], [[3],[4]]
    print(solution(arr1, arr2))





