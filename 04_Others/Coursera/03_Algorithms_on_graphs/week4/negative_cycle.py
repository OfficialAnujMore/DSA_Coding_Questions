# python3

from collections import namedtuple

def BellmanFord(n, graph):
    dist = [1001] * (n+1)
    dist[1] = 0
    prev = [None] * (n+1)
    negative_nodes = []
    
    for i in range(n):
        for u, v, w in graph:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                if i == n - 1:
                    negative_nodes.append(v)
                    
    if not negative_nodes:
        return 0
    else:
        return 1
        
if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = []
    
    for i in range(n_edges):
        a, b, w = map(int, input().split())
        edges.append((a, b, w)) 
        
    print(BellmanFord(n_vertices, edges))