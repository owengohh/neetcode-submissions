class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for c, p in prerequisites:
            adj[c].append(p)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(course):
            if states[course] == VISITING:
                return False
            if states[course] == VISITED:
                return True
            
            states[course] = VISITING

            for p in adj[course]:
                if not dfs(p):
                    return False
            
            states[course] = VISITED
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True