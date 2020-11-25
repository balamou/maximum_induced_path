from networkx.generators.random_graphs import erdos_renyi_graph
import matplotlib.pyplot as plt
import networkx as nx
import random


def several_rounds_induced(graph, iterations = 20): 
    """
    Keeps finding induced paths randomly and returns the one with the max length
    """
    max_induced_path = []
    
    for _ in range(iterations):
        found_induced_path = heuristic_induced_path(graph)
        print(f'Len: {len(found_induced_path)}, path: {found_induced_path}')
        if len(found_induced_path) > len(max_induced_path):
            max_induced_path = found_induced_path

    return max_induced_path


def heuristic_induced_path(graph):
    initial_node = pick_random_node(graph)
    visited = {initial_node}
    result = []
    current_node = initial_node

    while current_node != None:
        adjacent_nodes = list(graph.adj[current_node])

        result.append(current_node)

        current_node = pick_random_not_visited_node(adjacent_nodes, visited)
        visited.update(adjacent_nodes)

    return result

def pick_random_node(graph):
    """
    Pick a random node from the graph and return it.
    """
    nodes = list(graph.nodes)
    rand_index = pick_random_index(nodes)
    
    return nodes[rand_index]

def pick_random_not_visited_node(array, visited):
    """
    Picks a random non-visited node, if no such node can be found it returns None.
    """
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

    pos = nx.circular_layout(G) # Layout of the position of nodes
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 500)
    nx.draw_networkx_nodes(G, pos, nodelist=induced_path, cmap=plt.get_cmap('jet'), node_size = 500, node_color="red")
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=False)
    plt.show()

def main():
    total_nodes = 12 # total nodes created
    p = 0.2 # probability of edge creation
    graph = erdos_renyi_graph(total_nodes, p, 3245)
    print(list(graph.nodes))
    print(graph.edges)
    print(type(graph.edges))

    print(list(graph.adj[1]))

    heuristic = several_rounds_induced(graph)
    print("Heuristic solution:")
    print(f'Len: {len(heuristic)}, {heuristic}')
    draw(graph.edges, heuristic)

main()