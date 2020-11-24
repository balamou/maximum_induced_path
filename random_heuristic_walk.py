from networkx.generators.random_graphs import erdos_renyi_graph
import matplotlib.pyplot as plt
import networkx as nx
import random

n = 6
p = 0.5
g = erdos_renyi_graph(n, p)
print(list(g.nodes))
print(g.edges)
print(type(g.edges))

print(list(g.adj[1]))

def draw(edges):
    G = nx.DiGraph()
    G.add_edges_from(edges)

    # Need to create a layout when doing
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 500)
    # nx.draw_networkx_nodes(G, pos, nodelist=[first_node], cmap=plt.get_cmap('jet'), node_size = 500, node_color="red")
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=True)
    plt.show()

def heuristic_solution(graph, initial_node = 0):
    visited = {initial_node}
    result = []
    current_node = initial_node

    while current_node != None:
        adjacent_nodes = list(graph.adj[current_node])

        result.append(current_node)

        current_node = pick_random_node(adjacent_nodes, visited)
        visited.update(adjacent_nodes)

    return result


def pick_random_node(array, visited):
    index = pick_random_index(array)

    while len(array) > 0 and array[index] in visited:
        array.pop(index)
        index = pick_random_index(array)

    if len(array) == 0:
        return None

    return array[index]

def pick_random_index(array):
    if len(array) < 1:
        return None
    
    index = random.randint(0, len(array) - 1)
    return index

print(heuristic_solution(g))

draw(g.edges)
