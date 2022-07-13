class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        queue = collections.deque([root])
        
        while queue:
            level = []
            queue_len = len(queue)
            for _ in range(queue_len):
                current = queue.popleft()
                if current:
                    level.append(current.val)
                    
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
            
            if level:
                output.append(level)
        
        return output