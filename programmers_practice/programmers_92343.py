from collections import defaultdict, deque
from copy import deepcopy

is_wolf = list()
num2edges = defaultdict(list)
max_sheep = 0


def find_max_recursive(current_loc, used, nsheep, nwolf, can_go):
    global max_sheep

    if used[current_loc]: return  # 현재 노드를 방문한 경우 return
    used[current_loc] = True  # 방문 기록

    if is_wolf[current_loc]:  # 늑대인 경우 늑대 count += 1
        nwolf += 1
    else:
        nsheep += 1  # 양인 경우 양 count += 1
        max_sheep = max(max_sheep, nsheep)  # 양 최대 수 갱신
    if nsheep <= nwolf: return  # 늑대 수가 양의 수와 같거나 많은 경우 return

    can_go.extend(num2edges[current_loc])  # 현재 노드와 연결된 노드를 추가함
    for next_loc in can_go:
        # q에 저장된 노드서 하나를 가져와서 재귀함수 요청
        # 이 때 다음 q에는 현재 노드를 제외한 리스트로 재구성하여 재귀함수 요청
        find_max_recursive(next_loc, deepcopy(used), nsheep, nwolf,
                           can_go=[loc for loc in can_go if loc != next_loc and not used[loc]])


def solution(info, edges):
    global is_wolf, num2edges, max_sheep
    is_wolf = info  # 전역변수에 할당
    used = [False] * len(is_wolf)  # 방문한 노드 확인 용 변수

    for e_from, e_to in edges:
        num2edges[e_from].append(e_to)  # 연결된 엣지 리스트에 추가
    print(num2edges)
    for i, v in num2edges.items():
        print(i, ":", v)
    # start
    find_max_recursive(0, used, 0, 0, [])
    return max_sheep
