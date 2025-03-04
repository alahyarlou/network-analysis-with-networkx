import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Create a directed graph
G = nx.DiGraph()

# Add nodes
nodes = ['A', 'B', 'C', 'D', 'E']
G.add_nodes_from(nodes)

# Add edges
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A'), ('A', 'C')]
G.add_edges_from(edges)

# Display the directed graph
plt.figure(figsize=(6, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
plt.title("Directed Graph Visualization")
plt.show()

# Compute number of nodes and edges
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

print("Number of nodes:", num_nodes)
print("Number of edges:", num_edges)

print('-'*10)


# Check if a node exists in the graph
node_to_check = 'B'
node_exists = node_to_check in G

# Compute node degrees
degrees = {node: G.degree(node) for node in G.nodes()}

# Find neighbors of a node
neighbors_B = list(G.neighbors('B'))

# Create adjacency matrix
adj_matrix = nx.to_numpy_array(G)

# Remove a node and an edge
G.remove_node('E')
G.remove_edge('A', 'C')

# Extract a subgraph
subgraph_nodes = ['A', 'B', 'C']
sub_G = G.subgraph(subgraph_nodes)

# Assign weights to edges
weighted_G = nx.DiGraph()
weighted_edges = [('A', 'B', 5), ('B', 'C', 2), ('C', 'D', 3), ('D', 'A', 4)]
weighted_G.add_weighted_edges_from(weighted_edges)

# Display weighted graph
plt.figure(figsize=(6, 6))
pos = nx.spring_layout(weighted_G)
nx.draw(weighted_G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
edge_labels = nx.get_edge_attributes(weighted_G, 'weight')
nx.draw_networkx_edge_labels(weighted_G, pos, edge_labels=edge_labels)
plt.title("Weighted Graph Visualization")
plt.show()

# Convert directed graph to undirected
undirected_G = G.to_undirected()

# Display undirected graph
plt.figure(figsize=(6, 6))
nx.draw(undirected_G, with_labels=True, node_color='lightgreen', edge_color='black', node_size=2000, font_size=12)
plt.title("Undirected Graph Visualization")
plt.show()

# Display computed values
output = {
    "Number of Nodes": num_nodes,
    "Number of Edges": num_edges,
    f"Is Node '{node_to_check}' in Graph?": node_exists,
    "Node Degrees": degrees,
    "Neighbors of Node 'B'": neighbors_B,
    "Adjacency Matrix": adj_matrix
}
print(output)