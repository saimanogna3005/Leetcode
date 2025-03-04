class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list1=[]
        self.traversal(root,list1)
        return list1
    def traversal(self,root,list1):
        if root==None:
            return
        self.traversal(root.left,list1)
        list1.append(root.val)
        self.traversal(root.right,list1)