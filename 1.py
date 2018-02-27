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
    for current in vertices:
        if current not in visited:
            return dfs(current, graph, visited, color)


def dfs(parent, graph, visited, color):
    global bipartite
    for neighbor in graph[parent]:
        if neighbor not in visited:
            visited.append(neighbor)
            color[neighbor] = 1 - color[parent]
            dfs(neighbor, graph, visited, color)
        elif color[neighbor] == color[parent]:
            bipartite = "NO"
    return visited, color


def main():
    graph, vertices = create_graph()
    color = {str(_): 0 for _ in range(1, int(vertices) + 1)}
    visited, color = DFS(vertices, [], graph, color)
    print(bipartite)


if __name__ == '__main__':
    main()
