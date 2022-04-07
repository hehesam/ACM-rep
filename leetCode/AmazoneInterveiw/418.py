from collections import defaultdict, deque
class Solution:

    def findOrder(self, numCourses, pre_req):
        """
        :type numCourses: int
        :type pre_req: List[List[int]]
        :rtype: List[int]
        """

        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in pre_req:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        Q = deque([k for k in range(numCourses) if k not in indegree])

        res = []

        # Until there are nodes in the Q
        while Q:

            # Pop one node with 0 in-degree
            vertex = Q.popleft()
            res.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        Q.append(neighbor)

        return res if len(res) == numCourses else []