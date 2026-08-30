class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for p, q in prerequisites:
            adj[p].append(q)

        states = [0] * numCourses

        def dfs(c):
            if states[c] == 1:
                return False
            if states[c] == 2:
                return True
            
            states[c] = 1

            for p in adj[c]:
                if not dfs(p):
                    return False
            
            states[c] = 2
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True
