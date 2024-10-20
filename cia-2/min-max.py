import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, name, value=None, children=None):
        self.name = name
        self.initial_value = value
        self.final_value = None
        self.children = children or []

def min_max_search(node, depth, maximizer):
    if depth == 0 or not node.children:
        node.final_value = node.initial_value
        return node.final_value

    if maximizer:
        value = float('-inf')
        for child in node.children:
            value = max(value, min_max_search(child, depth - 1, False))
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, min_max_search(child, depth - 1, True))
    
    node.final_value = value
    return value

def create_tree():
    # Leaf nodes
    d = Node("D", 3)
    e = Node("E", 5)
    f = Node("F", 6)
    g = Node("G", 9)
    h = Node("H", 1)
    i = Node("I", 2)
    j = Node("J", 0)

    # Internal nodes
    b = Node("B", children=[d, e])
    c = Node("C", children=[f, g])
    k = Node("K", children=[h, i])
    l = Node("L", children=[j])

    # Root node
    a = Node("A", children=[b, c])
    m = Node("M", children=[k, l])

    # Top-level node
    root = Node("Root", children=[a, m])

    return root

def draw_tree(root, ax, pos=None, level=0, width=2., vert_gap = 0.2, xcenter = 0.5):
    if pos is None:
        pos = {root.name: (xcenter, 1 - level * vert_gap)}
    else:
        pos[root.name] = (xcenter, 1 - level * vert_gap)
    neighbors = root.children
    if neighbors:
        dx = width / 2
        nextx = xcenter - width/2 - dx/2
        for neighbor in neighbors:
            nextx += dx
            pos = draw_tree(neighbor, ax, pos=pos, level=level+1, width=dx, xcenter=nextx)
    return pos

def node_color(node, maximizing_level):
    if not node.children:
        return 'lightgreen'
    elif maximizing_level:
        return 'lightblue'
    else:
        return 'lightsalmon'

def show_graph(root, best_move):
    fig, ax = plt.subplots(figsize=(16, 10))
    fig.canvas.manager.set_window_title('Min-Max Tree')
    pos = draw_tree(root, ax)
    
    G = nx.Graph()
    
    def add_edges(node, level=0):
        color = node_color(node, level % 2 == 0)
        G.add_node(node.name, color=color)
        for child in node.children:
            G.add_edge(node.name, child.name)
            add_edges(child, level + 1)
    add_edges(root)
    
    node_colors = [G.nodes[node]['color'] for node in G.nodes()]
    nx.draw(G, pos, ax=ax, node_color=node_colors, node_size=3000, font_size=10, font_weight='bold')
    
    labels = {}
    for node in [root] + list(root.children) + [child for node in root.children for child in node.children]:
        if node.initial_value is not None:
            labels[node.name] = f"{node.name}\nInitial: {node.initial_value}\nFinal: {node.final_value}"
        elif node.final_value is not None:
            labels[node.name] = f"{node.name}\nFinal: {node.final_value}"
        else:
            labels[node.name] = node.name
    
    nx.draw_networkx_labels(G, pos, labels, font_size=8)
    
    legend_elements = [
        plt.Rectangle((0, 0), 1, 1, fc="lightblue", label="Maximizing"),
        plt.Rectangle((0, 0), 1, 1, fc="lightsalmon", label="Minimizing"),
        plt.Rectangle((0, 0), 1, 1, fc="lightgreen", label="Leaf Node")
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))
    
    ax.set_title("Min-Max Search Algorithm Visualization", fontsize=16, fontweight='bold')
    plt.text(0.5, -0.05, 
             "This graph shows the Min-Max search process on a game tree.\n"
             f"Best move: {best_move.name}\n"
             f"Best value: {best_move.final_value}",
             ha='center', va='center', transform=ax.transAxes, fontsize=10, wrap=True)
    
    plt.axis('off')
    plt.tight_layout()
    plt.show()


# create tree, perform min-max and display the results.
root = create_tree()

min_max_search(root, depth=3, maximizer=True)
best_move = max(root.children, key=lambda x: x.final_value)

show_graph(root, best_move)
