from collections import deque
# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Initialize the starting node and data structures
start = 'A'
queue = deque([start])  # Create a queue and enqueue the start node
visited = set([start])  # Create a set to track visited nodes

# Perform BFS
while queue:
    node = queue.popleft()  # Dequeue a node from the front of the queue
    print(node, end=" ")    # Process the node (here we print it)
    # Explore the neighbors of the current node
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)  # Mark the neighbor as visited
            queue.append(neighbor)  # Enqueue the neighbor
