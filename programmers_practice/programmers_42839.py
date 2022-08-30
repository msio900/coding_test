from itertools import permutations

n = 900000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

def solution(numbers):
    nums = []
    cards = list(numbers)
    # print(primes)
    for k in range(1, len(numbers)+1):
        for i in permutations(cards, k):
            num = ''
            for j in i:
                num += j
            num = int(num)
            if num in primes and num not in nums:
                nums.append(num)
    return len(nums)

if __name__ == '__main__':
    numbers = "17"
    print(solution(numbers))
    numbers = "011"
    print(solution(numbers))
