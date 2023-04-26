# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q, answer = deque(), []
        
        q.append(root)        
        while q:
            
            levelsize, total = len(q), 0
            for i in range(levelsize):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append( node.right)                
                total += node.val                
            answer.append( total/ levelsize )
            
        return answer
        