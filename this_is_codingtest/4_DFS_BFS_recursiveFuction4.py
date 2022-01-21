# 재귀함수를 이용하여 최대공약수 구현
def gcd(a, b):
    if a % b ==0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))