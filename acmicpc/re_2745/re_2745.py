import sys

input = sys.stdin.readline

n, b = input().split()

num = []
for i in n:
    if i.isupper():
        num.append(10+(ord(i)-ord('A')))
    else:
        num.append(int(i))

print(num)
answer = 0
for i in range(len(num)):
    print(f'{num[i]}*{int(b)}**{i} 전')
    print(f'{num[len(num)-i-1]}*{int(b)}**{i} 후')
    answer += num[len(num)-i-1]*int(b)**i
print(answer)

