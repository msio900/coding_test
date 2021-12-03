import sys

s = int(sys.stdin.readline())

for _ in range(s):
    sentence = sys.stdin.readline().split()
    answer = []
    for words in sentence:
        if len(words) == 1:
            answer.append(words)
        else:
            re_words = []
            for i in range(0, len(words)):
                re_words.append(words[- (i + 1)])
            re_words = "".join(re_words)
            answer.append(re_words)

    print(" ".join(answer))