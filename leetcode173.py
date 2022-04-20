#leetcode 173: Binary Search Tree Iterator
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.add_left_nodes(root)
    
    def add_left_nodes(self, node):
        if not node:
            return
        
        #add the current node to the stack before all left side nodes
        #(smaller values than node value)
        self.stack.append(node)
        
        #add all nodes on the left side of the stack
        #stack can grow to a max of O(h), h=height of tree
        while node.left:
            self.stack.append(node.left)
            node = node.left

    def next(self) -> int:
        #get next node from the stack and store it to return the value
        node = self.stack.pop()
        
        #add all left side nodes for the right child
        self.add_left_nodes(node.right)
        return node.val

    def hasNext(self) -> bool:
        #if the stack is empty, then there are no next values
        if self.stack:
            return True
        return False

