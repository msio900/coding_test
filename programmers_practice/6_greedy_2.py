
def solution(n, lost, reserve):
    answer = 0
    can_reserve = []
    for i in range(len(reserve)):
        can_reserve.append(reserve[i] - 1)
        can_reserve.append(reserve[i] + 1)
    for i in can_reserve:
        if i <= 0 or i >= n:
            can_reserve.remove(i)

    can_reserve = set(can_reserve)
    can_reserve = list(can_reserve)
    for i in range(1, n+1):
        if i in can_reserve:
            answer+=1
    return answer

if __name__ == '__main__':
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]
    print(solution(n, lost, reserve))