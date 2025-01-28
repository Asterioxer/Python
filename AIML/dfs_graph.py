graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : ['G', 'H'],
    'E' : [],
    'F' : [],
    'G' : [],
    'H' : ['I'],
    'I' : []
}

start_node = 'A'
visited = set()
stack = [start_node]
print("DFS Traversal Order: ")

while stack:
    cur_node = stack.pop()
    if cur_node not in visited:
        print(cur_node, end=" ")
        visited.add(cur_node)
        for neighbor in reversed(graph[cur_node]):
            if neighbor not in visited and cur_node == 'G':
                stack.append(neighbor)
                break
            
                
            