## 간편한 연결 리스트 구현 ##

# import sys
#
# input = sys.stdin.readline
#
# s = input().rstrip()
# n = int(input())
#
# mx =1000005
# dat = [-1]*mx
# pre = [-1]*mx
# nxt = [-1]*mx
#
# unused = 1
#
# def insert(addr:int, num:int):
#     global unused
#     dat[unused] = num
#     pre[unused] = addr
#     nxt[unused] = nxt[addr]
#     if nxt[addr] != -1:
#         pre[nxt[addr]] = unused
#     nxt[addr] = unused
#     unused += 1
#
# def erase(addr:int):
#     nxt[pre[addr]] = nxt[addr]
#     if nxt[addr] != -1:
#         pre[nxt[addr]] = pre[addr]
#
# def traverse():
#     cur = nxt[0]
#     while cur != -1:
#         print(dat[cur], end='')
#         cur = nxt[cur]
#
# cursor = 0
#
# for i in s:
#     insert(cursor, i)
#     cursor +=1
#
# for _ in range(n):
#     command = input().split()
#     if command[0] == 'L':
#         if pre[cursor] != -1:
#             cursor = pre[cursor]
#     elif command[0] == 'D':
#         if nxt[cursor] != -1:
#             cursor = nxt[cursor]
#     elif command[0] == 'B':
#         if pre[cursor] != -1:
#             erase(cursor)
#             cursor = pre[cursor]
#     else:
#         insert(cursor, command[1])
#         cursor = nxt[cursor]
# traverse()

# 정식 연결 리스트로 구현하기

# import sys
#
# class Node:
#     def __init__(self, item):
#         self.data = item
#         self.prev = None
#         self.next = None
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.nodeCount = 0
#         self.head = Node(None)
#         self.tail = Node(None)
#         self.head.prev = None
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.tail.next = None
#         self.cursor = self.tail
#
#     # 리스트 순회
#     def traverse(self):
#         result = []
#         curr = self.head
#         while curr.next.next:
#             curr = curr.next
#             result.append(curr.data)
#         return result
#
#     # 특정 원소 참조
#     def getAt(self, pos):  # getAt(0) -> head
#         if pos < 0 or pos > self.nodeCount:
#             return None
#
#         if pos > self.nodeCount // 2:
#             i = 0
#             curr = self.tail
#             while i < self.nodeCount - pos + 1:
#                 curr = curr.prev
#                 i += 1
#         else:
#             i = 0
#             curr = self.head
#             while i < pos:
#                 curr = curr.next
#                 i += 1
#         return curr
#
#     # 원소의 삽입
#     def insertAfter(self, prev, newNode):  # prev가 가리키는 node의 다음에 newNode를 삽입하고 성공/실패에 따라 True/False를 리턴
#         next = prev.next
#         newNode.prev = prev
#         newNode.next = next
#         prev.next = newNode
#         next.prev = newNode
#         self.nodeCount += 1
#         return True
#
#     def insertBefore(self, next, newNode):
#         prev = next.prev
#         newNode.prev = prev
#         newNode.next = next
#         prev.next = newNode
#         next.prev = newNode
#         self.nodeCount += 1
#         return True
#
#     def insertAt(self, pos, newNode):
#         if pos < 1 or pos > self.nodeCount + 1:
#             return False
#         prev = self.getAt(pos - 1)  # newNode가 삽입될 위치
#         return self.insertAfter(prev, newNode)
#
#     def popBefore(self, next):  # next의 이전에 있던 node를 삭제하고, 그 node의 data를 리턴
#         curr = next.prev
#         prev = curr.prev
#         prev.next = next
#         next.prev = prev
#         self.nodeCount -= 1
#         return curr.data
#
# input = sys.stdin.readline
#
# s = input().rstrip()
# n = int(input())
# linked_list = DoublyLinkedList()
#
# for i in range(len(s)):
#     linked_list.insertAt(i+1, Node(s[i]))
#
# for _ in range(n):
#     command = input().split()
#     if command[0] == 'L':
#         if linked_list.cursor.prev.prev:
#             linked_list.cursor = linked_list.cursor.prev
#     elif command[0] == 'D':
#         if linked_list.cursor.next:
#             linked_list.cursor = linked_list.cursor.next
#     elif command[0] == 'B':
#         if linked_list.cursor.prev.prev:
#             linked_list.popBefore(linked_list.cursor)
#     else:
#         node = Node(command[1])
#         linked_list.insertBefore(linked_list.cursor, node)
#
# print(''.join(linked_list.traverse()))

## 스택을 이용한 풀이 ##

import sys

input = sys.stdin.readline

L_stack = list(map(str, input().rstrip()))

M = int(input())

R_stack = []
# 커서의 위치는 명령어가 수행되기 전에는 맨 뒤에 위치하고 있음.
for _ in range(M):
    command = input().split()
    if command[0] == 'L' and L_stack :
        R_stack.append(L_stack.pop())

    if command[0] == 'D' and R_stack:
        L_stack.append(R_stack.pop())

    if command[0] == 'B'and L_stack:
        L_stack.pop()

    if command[0] == 'P':
        L_stack.append(command[1])

R_stack.reverse()
print(''.join(L_stack+R_stack))
