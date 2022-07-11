class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # edge case
        if not root:
            return []
        
        level, ret = [root], []
        while level:
            ret.append(level[-1].val)
            nextlevel = []
            for node in level:
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            level = nextlevel
        return ret