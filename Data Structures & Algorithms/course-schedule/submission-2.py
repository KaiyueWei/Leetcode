class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #make a graph
        #vertex is the course, if there is an edge from a to b meaning that b is the prerequisite of a
        graph = [ [] for _ in range(numCourses)]
        for prereq in prerequisites:
            course, prereq = prereq
            graph[course].append(prereq)
        #dfs check if there is cycle
        states = [0] * numCourses #0:unvisited, 1:visiting, 2:visited

        def dfs(course):
            if states[course] == 1:
                return False
            if states[course] == 2:
                return True
            states[course] = 1
            for preq in graph[course]:
                if not dfs(preq):
                    return False
            states[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
