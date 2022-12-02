class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root.left: 
            root.left = self.removeLeafNodes(root.left, target)
        if root.right: 
            root.right = self.removeLeafNodes(root.right, target)
        return None if root.left == root.right and root.val == target else root
