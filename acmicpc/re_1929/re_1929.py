import sys

input = sys.stdin.readline

M, N = map(int, input().split())

def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

for i in range(M, N + 1):
  if(isPrime(i)):
    print(i)