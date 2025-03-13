import heapq

def max_reliability(graph, max_connections):
    # Step 1: Create Priority Queue
    pq = []
    for u, v, reliability in graph:
        heapq.heappush(pq, (-reliability, u, v))

    # Step 2: Remove Excess Connections
    server_connections = {}
    selected_connections = []

    while pq:
        reliability, u, v = heapq.heappop(pq)

        if (u not in server_connections or server_connections[u] < max_connections) and \
           (v not in server_connections or server_connections[v] < max_connections):
            # Add the connection if it doesn't exceed the maximum connections for both servers
            selected_connections.append((-reliability, u, v))

            # Update connection counts for both servers
            server_connections[u] = server_connections.get(u, 0) + 1
            server_connections[v] = server_connections.get(v, 0) + 1

    # Step 3: Calculate Maximum Reliability
    max_reliability_sum = sum(reliability for reliability, _, _ in selected_connections)
    return max_reliability_sum

# Example usage:
graph = [(0, 1, 5), (1, 2, 8), (2, 3, 6), (1, 4, 7)]
max_connections = 2
result = max_reliability(graph, max_connections)
print(result)
    
