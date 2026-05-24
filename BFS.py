from collections import deque
e = int(input("Enter number of edges: "))
graph = {}
for _ in range(e):
    u, v = input("Enter edge (u v): ").split()   
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []       
    graph[u].append(v)
    graph[v].append(u)  
start = input("Enter starting node: ")
def bfs(graph, start) -> None:
    visited = set()
    queue = deque([start])   
    visited.add(start)
    print("\nBFS Traversal:")
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
bfs(graph, start)