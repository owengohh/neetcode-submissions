class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        adj = defaultdict(list)
        for p, c in prerequisites:
            adj[p].append(c)
        
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
            order.append(c)
            states[c] = 2
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order
        
        