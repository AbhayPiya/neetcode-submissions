class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n
        
        for x, y in edges:
            self.union(x, y)
        
        return self.components
    
    def find(self, x: int) -> int:
        # Path compression - recursive version (cleaner)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def find_iterative(self, x: int) -> int:
        # Path compression - iterative version
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        
        # Path compression
        while self.parent[x] != x:
            next_node = self.parent[x]
            self.parent[x] = root
            x = next_node
        
        return root
    
    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already connected
        
        # Union by rank
        if self.rank[root_y] > self.rank[root_x]:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]
        
        self.components -= 1
        return True  # Successfully merged
        

