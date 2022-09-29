import sys
from itertools import combinations

class Solution:
    def solution(self, n : list) -> list: # solution 함수 생성
        # print(n)
        answer = []
        for i in combinations(n, 7): # 9명의 난쟁이 중 7명의 난쟁이의 조합 도출
            if sum(i) == 100: # 조합 중 합이 100인 경우
                answer = list(i)
                break
        return sorted(answer) # 오름차순 정렬

if __name__ == '__main__':
    input = sys.stdin.readline
    heights = []
    # 9명의 난쟁이 키 받기
    for _ in range(9):
        heights.append(int(input().rstrip()))
    a_list = Solution().solution(n=heights)
    for i in a_list:
        print(i)