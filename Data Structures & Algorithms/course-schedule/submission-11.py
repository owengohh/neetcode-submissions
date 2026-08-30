class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for c, p in prerequisites:
            adj[c].append(p)
        
        UNVISITED = 0
        VISITED = 2
        VISITING = 1

        states = [UNVISITED] * numCourses

        def dfs(i):
            if states[i] == VISITING: return False
            if states[i] == VISITED: return True

            states[i] = VISITING

            for p in adj[i]:
                if not dfs(p):
                    return False
            
            states[i] = VISITED
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True