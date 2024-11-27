class Solution:
    from collections import deque, defaultdict

    def shortestPath(n, queries):
        # Initial graph setup (direct roads from i to i+1)
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)
        
        # Function to perform BFS and find the shortest path from city 0 to city n-1
        def bfs():
            # BFS to find shortest path from 0 to n-1
            queue = deque([0])
            distances = [-1] * n
            distances[0] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if distances[neighbor] == -1:  # Not visited
                        distances[neighbor] = distances[node] + 1
                        queue.append(neighbor)
            return distances[n - 1]  # Return the distance to city n-1, or -1 if not reachable
        
        answer = []
        
        # Process each query
        for u, v in queries:
            # Add the new road from u to v
            graph[u].append(v)
            # Find the shortest path from city 0 to city n-1 after the query
            shortest_path_length = bfs()
            answer.append(shortest_path_length)
        
        return answer

            