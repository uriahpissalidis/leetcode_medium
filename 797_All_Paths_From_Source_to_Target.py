class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        [] 0
        [0] 1
        [0, 1] 3
        result: [[0, 1, 3]]
        [0] 2
        [0, 2] 3
        result: [[0, 1, 3], [0, 2, 3]]
        """

        size = len(graph)
        result = []
        
        def dfs(path, vertex):
            if vertex == size-1:
                result.append(path + [vertex])
            else:
                for i in graph[vertex]: dfs(path + [vertex], i)
        dfs([], 0)
        
        return result