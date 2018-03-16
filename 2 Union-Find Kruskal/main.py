partition = {}
edges = []
path = []
weight = 0


def create_graph():
    global edges
    vertex_count, edge_count = input().split(' ')
    vertex_count = int(vertex_count)
    edge_count = int(edge_count)

    graph = {(_): [] for _ in range(1, (vertex_count + 1))}
    for count in range(edge_count):
        left, right, weight = input().split(' ')
        left = int(left)
        right = int(right)
        weight = int(weight)
        if right not in graph[left]:
            edges.append((left, right, weight))
            graph[left].append((left, right, weight))
    return graph


def root(vertex):
    global partition
    if partition[vertex] == {}:
        return vertex
    else:
        partition[vertex] = root(partition[vertex])
        return partition[vertex]


def mst_kruskal(graph):
    global edges, partition, path, weight
    for vertex in graph:
        partition[vertex] = {}
    edges.sort(key=lambda x: x[2])

    for edge in edges:
        u_prime = root(edge[0])
        v_prime = root(edge[1])
        if u_prime != v_prime:
            path.append(edge[:2])
            weight += edge[2]
            partition[u_prime] = v_prime
    return path


def main():
    graph = create_graph()
    mst_edges = sorted(mst_kruskal(graph), key=lambda y: y[0])
    print(weight)
    [print(edge[0],edge[1]) for edge in mst_edges]


if __name__ == '__main__':
    main()
