class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        count = 0           # number of redundant connections
        network = [i for i in range(n)]

        def find(x):
            if network[x] != x:
                network[x] = find(network[x])
            return network[x]
        
        def union(a, b):
            # return True if 2 nodes are already connected.
            root_a = find(a)
            root_b = find(b)
            network[root_a] = root_b
            return True if root_a == root_b else False
        
        for link in connections:
            if union(link[0], link[1]):
                count += 1

        # count the number of connected clusters
        a = len(set([find(i) for i in range(n)]))
        return -1 if a - 1 > count else a - 1
        