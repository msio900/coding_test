from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    positions = deque(range(len(priorities)))
    answer = 0
    while True:
        max_priority = max(priorities)
        if priorities[0] == max_priority:
            answer += 1
            if positions[0] == location:
                break
            priorities.popleft()
            positions.popleft()
        else:
            priorities.append(priorities.popleft())
            positions.append(positions.popleft())

    return answer

if __name__ =='__main__':
    priorities,	location = [2, 1, 3, 2], 2
    print(solution(priorities, location))
    priorities,	location = [1, 1, 9, 1, 1, 1], 0
    print(solution(priorities, location))