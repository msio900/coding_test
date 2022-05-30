import sys
import math

input = sys.stdin.readline

def lcm(a, b):
    return (a * b) //math.gcd(a, b)

a, b = list(map(int, input().split()))

print(math.gcd(a, b))
print(lcm(a, b))