import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add processes (P1, P2) and resources (R1, R2)
G.add_nodes_from(["P1", "P2"], type="process", color="lightblue")
G.add_nodes_from(["R1", "R2"], type="resource", color="orange")

# Add edges to represent assignments and requests
G.add_edge("P1", "R2", label="holds", style="solid")   # P1 holds R2
G.add_edge("R1", "P1", label="requests", style="dashed")  # P1 requests R1
G.add_edge("P2", "R1", label="holds", style="solid")   # P2 holds R1
G.add_edge("R2", "P2", label="requests", style="dashed")  # P2 requests R2

# Set node positions for clarity
pos = {
    "P1": (0, 1),
    "P2": (2, 1),
    "R1": (1, 0),
    "R2": (1, 2)
}

# Draw nodes with colors
node_colors = [G.nodes[n]["color"] for n in G.nodes]
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2000)

# Draw labels
nx.draw_networkx_labels(G, pos)

# Draw edges with styles
solid_edges = [(u, v) for (u, v, d) in G.edges(data=True) if d["style"] == "solid"]
dashed_edges = [(u, v) for (u, v, d) in G.edges(data=True) if d["style"] == "dashed"]
nx.draw_networkx_edges(G, pos, edgelist=solid_edges, arrowstyle="->", arrowsize=20)
nx.draw_networkx_edges(G, pos, edgelist=dashed_edges, style="dashed", arrowstyle="->", arrowsize=20)

# Add edge labels
edge_labels = {(u, v): d["label"] for (u, v, d) in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the plot
plt.title("Resource-Allocation Graph (Deadlock)")
plt.axis("off")
plt.show()