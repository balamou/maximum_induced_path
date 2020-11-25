from networkx.generators.random_graphs import erdos_renyi_graph
import matplotlib.pyplot as plt
import networkx as nx
import random


def find_maximum_induced_path(graph, iterations = 20): 
    """
    Keeps finding induced paths randomly and returns the one with the max length
    """
    max_induced_path = []
    iteration_found = 0
    
    for i in range(iterations):
        found_induced_path = heuristic_induced_path(graph)
        print(f'Iteration: {i}, Len: {len(found_induced_path)}, path: {found_induced_path}')
        if len(found_induced_path) > len(max_induced_path):
            max_induced_path = found_induced_path
            iteration_found = i
        
    print(f'Result found after iteration {iteration_found + 1} out of {iterations}')

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

def draw(edges, induced_path = [], highlight_edges = []):
    G = nx.DiGraph()
    G.add_edges_from(edges)

    pos = nx.circular_layout(G) # Layout of the position of nodes
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 500)
    nx.draw_networkx_nodes(G, pos, nodelist=induced_path, cmap=plt.get_cmap('jet'), node_size = 500, node_color="red")
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=set(edges) - set(highlight_edges), arrows=False)
    nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, edge_color="red", width = 2)
    plt.show()

def draw_large_graph(edges, induced_path = [], highlight_edges = []):
    G = nx.DiGraph()
    G.add_edges_from(edges)

    pos = nx.random_layout(G) # Layout of the position of nodes
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 50, node_color="black")
    nx.draw_networkx_nodes(G, pos, nodelist=induced_path, cmap=plt.get_cmap('jet'), node_size = 100, node_color="red")
    # nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=set(edges) - set(highlight_edges), arrows=False,edge_color="gray")
    nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, edge_color="red", width = 2)
    plt.show()

def convert_induced_nodes_to_edges(induced_nodes):
    result = []

    if len(induced_nodes) < 2:
        return induced_nodes

    for i in range(len(induced_nodes) - 1):
        result.append((induced_nodes[i], induced_nodes[i + 1]))

    return result


def generate_random_graph():
    total_nodes = 50  # total nodes created
    p = 0.10 # probability of edge creation
    seed = 6940 # seed
    return erdos_renyi_graph(total_nodes, p, seed)

def main():
    graph = generate_random_graph()

    maximum_induced_path = find_maximum_induced_path(graph, 100)

    print()
    print('Heuristic solution')
    print(f'Maximum induced path: {maximum_induced_path}')
    print(f'With length: {len(maximum_induced_path)}')
    edges = convert_induced_nodes_to_edges(maximum_induced_path)
    draw_large_graph(graph.edges, maximum_induced_path, edges)

main()
