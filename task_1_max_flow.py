from collections import deque
from task_1_graph import capacity_matrix


# function for finding an increasing path (BFS)
def bfs(capacity_matrix, flow_matrix, terminal, store, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([terminal])
    visited[terminal] = True

    while queue:
        current_node = queue.popleft()

        for neighbor in range(len(capacity_matrix)):
            # check if there is a residual bandwidth in the flow
            if (
                not visited[neighbor]
                and capacity_matrix[current_node][neighbor]
                - flow_matrix[current_node][neighbor]
                > 0
            ):
                parent[neighbor] = current_node
                visited[neighbor] = True
                if neighbor == store:
                    return True
                queue.append(neighbor)

    return False


def edmonds_karp(capacity_matrix, terminal, store):
    num_nodes = len(capacity_matrix)
    # initialize flow matrix with zeros
    flow_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    parent = [-1] * num_nodes
    max_flow = 0

    # while there is an increasing path add flow
    while bfs(capacity_matrix, flow_matrix, terminal, store, parent):
        # find the minimum residual bandwidth in the path
        path_flow = float("inf")
        current_node = store

        while current_node != terminal:
            previous_node = parent[current_node]
            path_flow = min(
                path_flow,
                capacity_matrix[previous_node][current_node]
                - flow_matrix[previous_node][current_node],
            )
            current_node = previous_node

        # update the flow matrix, taking into account the reverse path flow
        current_node = store

        while current_node != terminal:
            previous_node = parent[current_node]
            flow_matrix[previous_node][current_node] += path_flow
            flow_matrix[current_node][previous_node] -= path_flow
            current_node = previous_node

        # increase the maximum flow
        max_flow += path_flow

    return max_flow


# define the terminal and related stores
terminal_to_stores = {
    0: [6, 7, 8, 9, 10, 11, 12, 13, 14],
    1: [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
}

# display the results
print("=" * 50)
print(f"{'Terminal':^15} | {'Store':^15} | {'Max Flow':^15}")
# calculate the maximum flow for each terminal and store pair
for terminal, stores in terminal_to_stores.items():
    print("=" * 50)
    for store in stores:
        max_flow = edmonds_karp(capacity_matrix, terminal, store)
        print(f"{terminal:^15} | {store:^15} | {max_flow:^15}")
print("=" * 50)