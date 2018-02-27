# Author: Varun Shijo UB 50244968
# DFS for Graphs

bipartite = "YES"


def create_graph():
    vertices, edges = input().split(' ')

    # dictionary comprehension to initialize graph nodes
    graph = {str(_): [] for _ in range(1, int(vertices) + 1)}
    # read from stdin to populate edges
    for count in range(int(edges)):
        left, right = input().split(' ')
        if right not in graph[left]:
            graph[left].append(right)
        if left not in graph[right]:
            graph[right].append(left)
    return graph, vertices


def DFS(vertices, visited, graph, color):
    for s in vertices:
        if s not in visited:
            return dfs(s, graph, visited, color)


def dfs(v, graph, visited, color):
    global bipartite
    for u in graph[v]:
        if u not in visited:
            visited.append(u)
            color[u] = 1 - color[v]
            dfs(u, graph, visited, color)
        elif color[u] == color[v]:
            bipartite = "NO"
    return visited, color


def main():
    graph, vertices = create_graph()
    print(graph)
    color = {str(_): 0 for _ in range(1, int(vertices) + 1)}
    visited, color = DFS(vertices, [], graph, color)
    print(bipartite)


if __name__ == '__main__':
    main()
