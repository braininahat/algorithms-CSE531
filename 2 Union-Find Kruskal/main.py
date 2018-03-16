par = {}
edges = []
F = []
weight = 0


def create_graph():
    global edges
    vertex_count, edge_count = input().split(' ')
    vertex_count = int(vertex_count)
    edge_count = int(edge_count)

    # dictionary comprehension to initialize graph nodes
    graph = {(_): [] for _ in range(1, (vertex_count + 1))}
    # read from stdin to populate edges
    for count in range(edge_count):
        left, right, weight = input().split(' ')
        left = int(left)
        right = int(right)
        weight = int(weight)
        if right not in graph[left]:
            edges.append((left, right, weight))
            graph[left].append((left, right, weight))
        # if left not in graph[right]:
        #     edges.append((right, left, weight))
        #     graph[right].append((right, left, weight))
    return graph


def root(vertex):
    global par
    if par[vertex] == {}:
        return vertex
    else:
        par[vertex] = root(par[vertex])
        return par[vertex]


def mst_kruskal(graph):
    global edges, par, F, weight
    for vertex in graph:
        par[vertex] = {}
    #     graph[vertex].sort(key=lambda x: x[2])
    # print(par)
    edges.sort(key=lambda x: x[2])

    for edge in edges:
        u_prime = root(edge[0])
        v_prime = root(edge[1])
        if u_prime != v_prime:
            F.append(edge[:2])
            weight += edge[2]
            par[u_prime] = v_prime
    return F


def main():
    graph = create_graph()
    # print(graph)
    mst_edges = sorted(mst_kruskal(graph), key=lambda y: y[0])
    print(weight)
    [print(edge[0],edge[1]) for edge in mst_edges]


if __name__ == '__main__':
    main()
