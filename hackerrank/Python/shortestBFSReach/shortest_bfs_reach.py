from collections import defaultdict, deque

"""
   Graph with function to get the shortest distance
   to each other node from a starting node
   Runs breadth first, distance per edge is 6
   Modified to run with input files
"""

class Graph:
    """Bidirectional graph"""

    def __init__(self, n):
        """Initialises the node count and edge dict

        Arguments:
            n {integer} -- Number of nodes, 1-indexed
        """

        self.node_count = n
        self.edges = defaultdict(list)

    def connect(self, x, y):
        if y not in self.edges[x]:
            self.edges[x].append(y)
        if x not in self.edges[y]:
            self.edges[y].append(x)

    # Gets all nodes connected at the current depth,
    # then adds all of the following nodes on to the queue.
    def find_all_distances(self, start, edge_length=1):
        """Breadth first search to get a list of distances
        to all nodes connected to the starting node.
        
        Arguments:
            start {integer} -- The starting node value.
            edge_length {integer} -- The length per edge.
        
        Returns:
            list -- A list containing the shortest distance
            to all nodes connected to start. -1 if no path.
        """

        depth = 1
        distances = [-1] * (self.node_count + 1)
        distances[start] = 0
        q = deque(self.edges[start])
        while q:
            connections_at_curr_depth = list(q)
            for node in connections_at_curr_depth:
                if distances[node] == -1:
                    distances[node] = depth * edge_length
                    q.extend(self.edges[node])
                q.popleft()
            depth += 1
        del distances[start]
        # 1 indexed, delete first item
        del distances[0]
        return distances
