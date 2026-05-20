class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[False] * numCourses for _ in range(numCourses)]

        for pre, crs in prerequisites: adj[pre][crs] = True

        for k in range(numCourses):
            for i in range(numCourses):
                if adj[i][k]:
                    for j in range(numCourses):
                        if adj[k][j]: adj[i][j] = True
        
        res = []
        for u,v in queries: res.append(adj[u][v])

        return res