from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=deque()
        queue.append(root)
        ans=[]
        while queue:
            l=[]
            for i in range(len(queue)):
                cur=queue.popleft()
                l.append(cur.val)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            ans.append(l)
        return ans

        