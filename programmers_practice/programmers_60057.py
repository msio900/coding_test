def solution(s):
    answer =1e9
    if len(s) < 3:
        return len(s)
    for i in range(1,len(s)//2+1):
        cnt=1
        strr=""
        pre=s[0:i]
        for j in range(i,len(s)+i,i):
            if pre == s[j:j+i]:
                cnt+=1
            else:
                if cnt !=1:
                    strr+=str(cnt)+pre
                else:
                    strr+=pre
                cnt=1
                pre=s[j:j+i]
        answer = min(ans,len(strr))
    return answer

if __name__ =='__main__':
    s = "aabbaccc"
    print(solution(s))
    s = "ababcdcdababcdcd"
    print(solution(s))
    s = "abcabcdede"
    print(solution(s))
    s = "abcabcabcabcdededededede"
    print(solution(s))
    s = "xababcdcdababcdcd"
    print(solution(s))





