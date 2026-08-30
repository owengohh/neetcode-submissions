class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for c, p in prerequisites:
            adj[c].append(p)
        
        # 0 -> unvisited
        # 1 -> visiting
        # 2 -> visited

        states = [0] * numCourses

        def dfs(c):
            state = states[c]
            if state == 1:
                return False
            if state == 2:
                return True
            
            states[c] = 1
            
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            
            states[c] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True