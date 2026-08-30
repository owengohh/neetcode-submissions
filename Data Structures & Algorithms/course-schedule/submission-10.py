class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for c, p in prerequisites:
            adj[c].append(p)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(c):
            if states[c] == VISITED:
                return True
            if states[c] == VISITING:
                return False
            
            states[c] = VISITING
            for pre in adj[c]:
                if not dfs(pre):
                    return False
            
            states[c] = VISITED
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
