from networkx.generators.random_graphs import erdos_renyi_graph
import matplotlib.pyplot as plt
import networkx as nx

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

draw(g.edges)