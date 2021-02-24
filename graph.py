class UndirectedGraph:

    def __init__(self, filename=""):
        self.nodes = []
        self.edges = {}
        if filename:
            self.load_from_csv(filename)

    def load_from_csv(self, filename):
        """
        :param filename: a graph representation where:
         - each line represents an edge
         - each edge is a comma-separated values of the 2 connected nodes and its cost
        """
        with open(filename) as graph_file:
            for line in graph_file:
                items = line.strip().split(',')
                if len(items) != 3:
                    raise ValueError("Graph file contains an invalid line: " + line)
                node1, node2, cost = items
                if not cost.isnumeric():
                    raise ValueError("Graph file contains non-numeric cost: " + cost)
                if int(cost) < 0:
                    raise ValueError("Graph file contains negative cost: " + cost)
                if not node1.isnumeric():
                    self.add_node(node1)
                if not node2.isnumeric():
                    self.add_node(node2)
                if node2 in self.edges[node1] and int(cost) != self.edges[node1][node2]:
                    raise ValueError("Graph file contains conflicting edge: " + line)
                self.add_edge(node1, node2, cost)

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes.append(name)
            self.edges[name] = {}

    def add_edge(self, node1, node2, cost):
        if node1 in self.nodes and node2 in self.nodes:
            self.edges[node1][node2] = int(cost)
            self.edges[node2][node1] = int(cost)

    def shortest_path(self, start, end):
        assert start in self.nodes and end in self.nodes

        if start == end:
            return {'path': [start], 'cost': 0}

        if end in self.edges[start]:
            return {'path': [start, end], 'cost': self.edges[start][end]}

        current_node = start
        visited = [start]
        options = self.paths_from(start)
        min_cost = float('inf')
        min_path = None

        while len(options) != 0:
            # Start expanding from min so our first visit is optimal
            # (unless we allow negative costs)
            min_option = min(options, key=lambda option: option['cost'])
            options.remove(min_option)
            path = min_option['path']
            cost = min_option['cost']
            current_node = path[-1]
            if cost >= min_cost:
                continue

            expansions = self.paths_from(current_node)
            for expansion in expansions:
                expansion_node = expansion['path'][-1]
                if expansion_node in visited:
                    continue
                else:
                    visited.append(expansion_node)

                next_path = path.copy()
                next_path.append(expansion_node)
                next_cost = cost + expansion['cost']
                if next_cost > min_cost:
                    continue
                
                if expansion_node == end:
                    if next_cost < min_cost:
                        min_cost = next_cost
                        min_path = next_path
                else:
                    next_option = {'path': next_path, 'cost': next_cost}
                    options.append(next_option)
        
        return {'path': min_path, 'cost': min_cost}

    def paths_from(self, node):
        assert node in self.nodes

        paths = []
        for adjacent_node, cost in self.edges[node].items():
            item = {'path': [node, adjacent_node], 'cost': cost}
            paths.append(item)
        return paths
