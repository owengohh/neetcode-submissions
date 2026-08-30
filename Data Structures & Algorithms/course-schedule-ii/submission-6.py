class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []

        adj = defaultdict(list)
        for c, p in prerequisites:
            adj[c].append(p)
        
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
            order.append(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order