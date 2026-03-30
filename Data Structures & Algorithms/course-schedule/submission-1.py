class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[course].append(pre)

        visiting = set()
        visited = set()

        def dfs(c):
            if c in visiting:   # cycle detected
                return True
            if c in visited:    # already checked, no cycle here
                return False

            visiting.add(c)
            for pre in graph[c]:
                if dfs(pre):
                    return True
            visiting.remove(c)
            visited.add(c)
            return False

        for i in range(numCourses):
            if dfs(i):
                return False

        return True

        