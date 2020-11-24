from networkx.generators.random_graphs import erdos_renyi_graph
import matplotlib.pyplot as plt
import networkx as nx
import random

def heuristic_induced_path(graph, initial_node = 0):
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

def draw(edges, induced_path = []):
    G = nx.DiGraph()
    G.add_edges_from(edges)

    # Need to create a layout when doing
    pos = nx.planar_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 500)
    nx.draw_networkx_nodes(G, pos, nodelist=induced_path, cmap=plt.get_cmap('jet'), node_size = 500, node_color="red")
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=False)
    plt.show()

def main():
    total_nodes = 6
    p = 0.5 # probability of edge creation
    graph = erdos_renyi_graph(total_nodes, p, 2493)
    print(list(graph.nodes))
    print(graph.edges)
    print(type(graph.edges))

    print(list(graph.adj[1]))

    heuristic = heuristic_induced_path(graph)
    print("Heuristic solution:")
    print(heuristic)
    draw(graph.edges, heuristic)

main()