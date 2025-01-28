V = 4

# Adjacency matrix representing the graph
# 0 means no edge, 1 means there is an edge
graph = [
    [0, 1, 1, 0],  # Node 0 is connected to nodes 1 and 2
    [1, 0, 1, 1],  # Node 1 is connected to nodes 0, 2, and 3
    [1, 1, 0, 1],  # Node 2 is connected to nodes 0, 1, and 3
    [0, 1, 1, 0]   # Node 3 is connected to nodes 1 and 2
]

# Number of colors
m = 3  # We are trying to use at most 3 colors

# List to store the color assigned to each vertex
colors = [-1] * V  # -1 indicates that no color has been assigned yet

# Backtracking algorithm to assign colors to the vertices
def is_safe(vertex, color, colors, graph):
    # Check all adjacent vertices to ensure no adjacent vertex has the same color
    for i in range(V):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
    return True

def graph_coloring(graph, m, colors, vertex):
    # Base case: if all vertices are assigned a color, return True
    if vertex == V:
        return True

    # Try different colors for vertex
    for color in range(m):
        if is_safe(vertex, color, colors, graph):
            colors[vertex] = color  # Assign color to vertex
            # Recur to assign colors to the next vertex
            if graph_coloring(graph, m, colors, vertex + 1):
                return True
            # If assigning color does not lead to a solution, backtrack
            colors[vertex] = -1

    return False  # If no color can be assigned to this vertex, return False

# Start coloring the graph
if graph_coloring(graph, m, colors, 0):
    # Print the solution if found
    print("Solution found:")
    for vertex in range(V):
        print(f"Vertex {vertex} -> Color {colors[vertex]}")
else:
    print("No solution exists.")
