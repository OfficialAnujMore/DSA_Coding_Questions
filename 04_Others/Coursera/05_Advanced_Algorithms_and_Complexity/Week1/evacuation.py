# python3

from collections import deque

def has_path(gf, path):
    n = len(gf)
    visited = [False] * n
    visited[0] = True
    queue = deque([0])
    while queue:
        temp = queue.popleft()
        if temp == n - 1:
            return True
        for i in range(n):
            if not visited[i] and gf[temp][i] > 0:
                queue.append(i)
                visited[i] = True
                path[i] = temp
    return visited[n-1]


def max_flow(gf):
    flow = 0
    n = len(gf)
    path = list(range(n))
    while has_path(gf, path):
        min_flow = float('inf')
        v = n - 1
        while v != 0:
            u = path[v]
            min_flow = min(min_flow, gf[u][v])
            v = u
        v = n - 1
        while v != 0:
            u = path[v]
            gf[u][v] -= min_flow
            gf[v][u] += min_flow
            v = u
        flow += min_flow
    return flow


if __name__ == '__main__':
    n_city, n_edges = map(int, input().split())
    residual_graph = [[0] * n_city for i in range(n_city)]
    
    for _ in range(n_edges):
        u, v, capacity = map(int, input().split())
        residual_graph[u - 1][v - 1] += capacity
        
    mf = max_flow(residual_graph)
    print(mf)