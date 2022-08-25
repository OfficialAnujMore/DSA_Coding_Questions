# python3

from collections import deque


def is_bipartite(n_vertices, adj_list):
    dist = [float('inf')] * (n_vertices+1)
    queue = deque()
    queue.append(1)
    dist[1] = 0

    while queue:
        current = queue.popleft()
        for vertex in adj_list[current]:
            if dist[vertex] == float('inf'):
                queue.append(vertex)
                dist[vertex] = dist[current] + 1
            elif (dist[current] - dist[vertex]) % 2 == 0:
                return 0

    return 1


if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())

    adjacency_list = [[] for _ in range(n_vertices+1)]

    for _ in range(n_edges):
        a, b = map(int, input().split())
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)

    print(is_bipartite(n_vertices, adjacency_list))
