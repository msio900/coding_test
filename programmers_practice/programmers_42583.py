from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    bridge = deque(bridge)
    while True:
        answer += 1
        if sum(list(bridge)[:-1]) + truck_weights[0] <= weight:
            bridge.appendleft(truck_weights.pop(0))
            bridge.pop()
            print(bridge)
        elif sum(list(bridge)[:-1]) + truck_weights[0] > weight:
            bridge.appendleft(0)
            bridge.pop()
            print(bridge)
        if not truck_weights and sum(bridge) == 0:
            print(bridge)
            break
    return answer

if __name__ =='__main__':
    bridge_length, weight, truck_weights = 2, 10, [7,4,5,6]
    print(solution(bridge_length, weight, truck_weights))
    bridge_length, weight, truck_weights = 100, 100, [10]
    print(solution(bridge_length, weight, truck_weights))
    bridge_length, weight, truck_weights = 100, 100, [10,10,10,10,10,10,10,10,10,10]
    print(solution(bridge_length, weight, truck_weights))