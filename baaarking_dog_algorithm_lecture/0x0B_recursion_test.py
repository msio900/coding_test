# n 부터 1까지 출력하는 함수

def func1(n : int):
    if n == 0:
        return
    print(n)
    func1(n - 1)
print('n 부터 1까지 출력하는 함수')
func1(10)
print('-'*120)

# 1부터 n까지 더하는 함수
def func2(n : int):
    if n == 0:
        return 0
    return n + func2(n - 1)

print('1부터 n까지 더하는 함수')
print(func2(10))
print('-'*120)