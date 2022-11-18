# 파이썬에서 무한대에 대한 규정
# import sys
# from math import inf
#
# mx = float('INF')
#
# print(mx)
#
# mx = sys.maxsize
#
# print(mx)
#
# mx = inf
#
# print(mx)
import sys

mx = 1000005
dat = [0]*(2*mx+1)
tail, head = mx, mx

def push_front(x : int):
    global head
    head -= 1
    dat[head] = x

def push_back(x : int):
    global tail
    dat[tail] = x
    tail +=1

def pop_front():
    head += 1

def pop_back():
    tail -= 1

def front():
    return dat[head]

def back():
    return dat[tail-1]

push_back(1)
print('f : ', front(),'b : ', back())
pop_back()
print('f : ', front(),'b : ', back())

push_back(2)
print('f : ', front(),'b : ', back())
push_back(3)
print('f : ', front(),'b : ', back())
push_back(4)
print('f : ', front(),'b : ', back())
push_back(5)
print('f : ', front(),'b : ', back())

