class Graph:
    def __init__(self, edges):
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                newpaths = self.get_paths(node, end, path)
                paths.extend(newpaths)
        return paths

    def get_shortest_path(self, start, end):
        paths = self.get_paths(start, end)
        shortest = None
        for path in paths:
            if shortest is None or len(path) < len(shortest):
                shortest = path
        return shortest


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune", "Hyderabad"),
        ("Pune", "Mysuru"),
        ("Hyderabad", "Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "Bangaluru"

    print(route_graph.get_paths(start, end))
    print(route_graph.get_shortest_path(start, end))
