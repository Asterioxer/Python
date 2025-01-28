import heapq

def a_star_search(graph, start, goal, heuristic):
    """
    A\* search algorithm.

    Args:
        graph: A dictionary representing the graph, where each key is a node and
            each value is a dictionary of neighboring nodes and their costs.
        start: The starting node.
        goal: The goal node.
        heuristic: A function that estimates the cost from a node to the goal.

    Returns:
        A list of nodes representing the shortest path from the start to the goal.
    """
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            break

        for neighbor, cost in graph[current].items():
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    # Reconstruct the path
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Example usage:
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 3, 'D': 1},
    'D': {'B': 2, 'C': 1}
}

def heuristic(node, goal):
    # Manhattan distance heuristic
    coordinates = {'A': (0, 0), 'B': (1, 0), 'C': (0, 1), 'D': (1, 1)}
    return abs(coordinates[node][0] - coordinates[goal][0]) + abs(coordinates[node][1] - coordinates[goal][1])

start = 'A'
goal = 'D'
path = a_star_search(graph, start, goal, heuristic)
print(path)  # Output: ['A', 'B', 'D']