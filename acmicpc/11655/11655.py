import sys

S = sys.stdin.readline().rstrip()

upper = [chr(i) for i in range(ord('A'), ord('Z')+1)]*2
lower = [chr(i) for i in range(ord('a'), ord('z')+1)]*2

sentence_list = []
for i in S:
    if 65 <= ord(i) <= 90:
        sentence_list.append(upper[ord(i)-65+13])
    elif 97 <= ord(i) <= 122:
        sentence_list.append(lower[ord(i)-97+13])
    else:
        sentence_list.append(i)

print(''.join(sentence_list))
