from collections import defaultdict

def solution(clothes):
    answer = 0
    category = defaultdict(int)
    for i in clothes:
        # print(i)
        category[i[1]] += 1
    cate_clothes = list(category.values())
    answer += sum(cate_clothes)

    return answer

if __name__ =='__main__':
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))
    clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    print(solution(clothes))