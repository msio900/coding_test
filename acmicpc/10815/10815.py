import sys

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
nums = [0]*len(alphabet)


s = sys.stdin.read()
# print(s)
for i in s:
    if i in alphabet:
        nums[ord(i) - ord('a')] += 1
answer = []
for k, v in enumerate(nums):
    if v == max(nums):
        answer.append(alphabet[k])
print(''.join(answer))
