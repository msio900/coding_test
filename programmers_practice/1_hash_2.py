def solution(phone_book):
    answer = True
    head = phone_book[0]
    phone_book.sort()
    print(phone_book)
    for i in phone_book[1:]:
        if i[:len(head)] == head:
            answer = False
            break

    return answer


if __name__ == '__main__':
    phone_book = ["119", "97674223", "1195524421"]
    print(solution(phone_book))