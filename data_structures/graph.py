"""
GRAPHS:
    - nodes connected by edges
    - multiple paths between nodes
        - difference between trees (trees have only one path)

DIRECTED GRAPHS:
    - edges have direction

WEIGHTED GRAPHS:
    - edges have weights (a cost to go from one node to another)

"""



class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.dic = {}
        for start, end in self.edges:
            if start in self.dic:
                self.dic[start].append(end)
            else:
                self.dic[start] = [end]


    def get_paths(self, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.dic:
            return []

        paths = []

        for node in self.dic[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        
        if start not in self.dic:
            return None
        
        if start == end:
            return path

        shortest_path = None
        for node in self.dic[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


def build_graph():
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)
    return route_graph
    

if __name__ == "__main__":
    g = build_graph()
    print(g.get_paths("Mumbai", "New York"))
    print(g.get_shortest_path("Mumbai", "New York"))