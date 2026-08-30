class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for c, p in prerequisites:
            g[c].append(p)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(course):
            if states[course] == VISITED: return True
            if states[course] == VISITING: return False

            states[course] = VISITING

            for nei in g[course]:
                if not dfs(nei):
                    return False
                
            states[course] = VISITED

            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True