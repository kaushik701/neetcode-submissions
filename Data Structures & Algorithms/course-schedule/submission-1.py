class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for course , pre in prerequisites:
            preMap[course].append(pre)
        visit = set()

        def dfs(course):
            if course in visit: return False
            if not preMap[course]: return True

            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            visit.remove(course)

            preMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        return True