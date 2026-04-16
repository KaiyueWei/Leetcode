class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## create a graph: node: course, edge: course a is a pre of course b, then an edge from b to an
        graph = [ [] for _ in range(numCourses)]

        for pair in prerequisites:
            course = pair[0]
            pre = pair[1]
            graph[course].append(pre)

        visiting = set()
        visited = set()
        ## detect a cycle
        def dfs(course):
            if course in visiting:
                return True
            if course in visited:
                return False
            visiting.add(course)
            for pre in graph[course]:
                if dfs(pre):
                    return True
            visited.add(course)
            visiting.remove(course)
            return False
        
        
        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True
        