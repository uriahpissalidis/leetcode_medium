class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        A = []
        def inorder(head):
            if head is None:
                return 
            inorder(head.left)
            A.append(head.val)
            inorder(head.right)
            
        inorder(root)
        # print(A)
        
        n = len(A)
        from bisect import bisect_left
        res = []
        for q in queries:
            i = bisect_left(A, q)
            # print(A,i,q)
            if i == n:
                res.append( [ A[i-1] , -1  ]  )
            elif A[i] == q:
                res.append( [ A[i] , A[i]  ]  )
            elif i == 0:
                res.append( [ -1 , A[i]  ]  )
            
            else:
                res.append( [ A[i-1] , A[i]  ]  )
        return res
