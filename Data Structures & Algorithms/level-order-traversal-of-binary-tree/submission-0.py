# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque([(root,0)])
        level=0
        answer=[]
        while queue:
            current,l=queue.popleft()
            if l == len(answer):
                answer.append([current.val])
            else:
                answer[l].append(current.val)

            if current.left:
                queue.append((current.left,l+1))
            if current.right:
                queue.append((current.right,l+1))

        return answer






        