# 230. Kth Smallest Element in a BST[↩](../programmers_practice)

[230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

## 🖋️문제

- Given the `root` of a binary search tree, and an integer `k`, return *the* `kth` *smallest value (**1-indexed**) of all the values of the nodes in the tree*.

   

  **Example 1:**

  ![img](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

  ```
  Input: root = [3,1,4,null,2], k = 1
  Output: 1
  ```

  **Example 2:**

  ![img](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

  ```
  Input: root = [5,3,6,2,4,null,null,1], k = 3
  Output: 3
  ```

   

  **Constraints:**

  - The number of nodes in the tree is `n`.
  - `1 <= k <= n <= 104`
  - `0 <= Node.val <= 104`

   

  **Follow up:** If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

## 💡풀이

### 1차 시도

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
```

* 채점 결과

```python

```

### 실패😂

* 