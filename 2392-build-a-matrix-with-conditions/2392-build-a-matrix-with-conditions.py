from collections import deque, defaultdict

class Solution:
    def topological_sort(self, k, conditions):
        adj_list = defaultdict(list)
        in_degree = [0] * (k + 1)

        for u, v in conditions:
            adj_list[u].append(v)
            in_degree[v] += 1

        
        queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in adj_list[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) == k:
            return topo_order
        else:
            return []

    def buildMatrix(self, k, rowConditions, colConditions):
        row_order = self.topological_sort(k, rowConditions)
        col_order = self.topological_sort(k, colConditions)

        if not row_order or not col_order:
            return []

        row_position = {value: idx for idx, value in enumerate(row_order)}
        col_position = {value: idx for idx, value in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for number in range(1, k + 1):
            row_idx = row_position[number]
            col_idx = col_position[number]
            matrix[row_idx][col_idx] = number

        return matrix

