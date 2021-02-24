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
                    raise ValueError("Provided graph file contains an invalid line: " + line)
                node1, node2, cost = items
                self.add_node(node1)
                self.add_node(node2)
                self.add_edge(node1, node2, cost)

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes.append(name)
            self.edges[name] = {}

    def add_edge(self, node1, node2, cost):
        self.edges[node1][node2] = int(cost)
        self.edges[node2][node1] = int(cost)

    def shortest_path(self, start, end):
        assert start in self.nodes and end in self.nodes

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
            #print("Expanding: ", path, cost)
            current_node = path[-1]
            if cost >= min_cost:
                continue

            expansions = self.paths_from(current_node)
            for expansion in expansions:
                #print("Considering: ", expansion['path'], expansion['cost'])
                expansion_node = expansion['path'][-1]
                if expansion_node in visited:
                    #print("\tAlready visited: ", expansion_node)
                    continue
                else:
                    visited.append(expansion_node)
                    #print("\tVisited: ", visited)

                next_path = path.copy()
                next_path.append(expansion_node)
                next_cost = cost + expansion['cost']
                if next_cost > min_cost:
                    #print("\tToo expensive: ", next_cost)
                    continue
                
                if expansion_node == end:
                    #print("\tEnd node")
                    if next_cost < min_cost:
                        #print("\tUpdate min: ", next_cost)
                        min_cost = next_cost
                        min_path = next_path
                else:
                    #print("\tAdd to option: ", next_path, next_cost)
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
