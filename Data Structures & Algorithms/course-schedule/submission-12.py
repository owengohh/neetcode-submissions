class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for c, p in prerequisites:
            adj[c].append(p)
        
        UNV = 0
        VIS = 1
        VID = 2

        states = [UNV] * numCourses
        
        def dfs(c):
            if states[c] == VIS:
                return False
            if states[c] == VID:
                return True
            
            states[c] = VIS

            for p in adj[c]:
                if not dfs(p):
                    return False
            
            states[c] = VID
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True