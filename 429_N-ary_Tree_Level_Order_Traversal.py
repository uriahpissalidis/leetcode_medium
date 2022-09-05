class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return
        ans = []
        def bfs(nodes):
            if not nodes:
                return
            children, nextNodes = [], []
            for node in nodes:
                children.append(node.val)
                nextNodes += node.children
            ans.append(children)
            bfs(nextNodes)
        ans.append([root.val])
        bfs(root.children)
        return ans