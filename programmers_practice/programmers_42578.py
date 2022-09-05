def solution(clothes):
    answer = 0
    df = pd.DataFrame(clothes)
    print(df[1].unique())

    return answer

if __name__ =='__main__':
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))
    clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    print(solution(clothes))






