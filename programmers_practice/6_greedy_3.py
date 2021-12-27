def solution(name):

    # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    answer = 0
    alpha = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    name_loc = [ord(i) - ord('A') for i in name]
    print(name_loc)
    return answer

if __name__ == '__main__':
    name = "JEROEN"
    print(solution(name))



# 1234123412341234
# 1234123412341234
# ________________


def solution(name):
    # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # JAZ
    # 앞으로 가는게 최선일지 뒤로 가는게 최선일지?
    # A일 경우 A를 지나서 가는게 나을지? 거꾸로 가는게 나을지? if i >= len(name)/2
    # A가 아닐경우
    # 위 아래로 움직이는 것은? n : -13 / +13
    # JDDDDFFEREFDFDFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD
    answer = 0
    alpha = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    name_loc = [ord(i) - ord('A') for i in name]
    print(name_loc)

