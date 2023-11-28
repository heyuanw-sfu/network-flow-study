import os

class Vertex:
    def __init__(self, name):
        self.name = name

class SimpleGraph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def insert_vertex(self, name):
        vertex = Vertex(name)
        self.vertices[name] = vertex
        return vertex

    def insert_edge(self, v1, v2, weight, name=None):
        edge = (v1, v2, weight, name)
        self.edges.append(edge)

class GraphInput:
    @staticmethod
    def load_simple_graph(newgraph, pathandfilename):
        if not os.path.exists(pathandfilename):
            print(f"File {pathandfilename} not found")
            return None

        table = {}
        line_count = 0

        with open(pathandfilename, 'r') as file:
            for line in file:
                line_count += 1
                tokens = line.split()

                if len(tokens) == 3:
                    v1name, v2name, edge_weight = tokens
                    edge_weight = float(edge_weight)

                    v1 = table.get(v1name) or newgraph.insert_vertex(v1name)
                    v2 = table.get(v2name) or newgraph.insert_vertex(v2name)
                    table[v1name] = v1
                    table[v2name] = v2

                    newgraph.insert_edge(v1, v2, edge_weight)
                else:
                    print(f"Error: Invalid number of tokens found on line {line_count}!")
                    return None

        print(f"Successfully loaded {line_count} lines.")
        return table

# # Example usage
# G = SimpleGraph()
# GraphInput.load_simple_graph(G, 'path_to_file.txt')
