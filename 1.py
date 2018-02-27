# Author: Varun Shijo UB 50244968
# DFS for Graphs

flag = "YES"


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


def dfs(graph, current, visited, color):
    # Traversal
    global flag
    neighbors = [str(_) for _ in graph[current]]
    if current not in visited:
        visited.append(current)
        if current != '1':
            color[current] = 1 - color[str(int(current) - 1)]
        for neighbor in neighbors:
            dfs(graph, neighbor, visited, color)
            if color[neighbor] == color[current]:
                flag = "NO"

    return visited, color


# def bipartite(graph, color):
#     for vertex in graph:
#         neighbors = [_ for _ in graph[vertex]]
#         color_list = [color[neighbor] for neighbor in neighbors]
#         if color[vertex] in color_list:
#             return "NO"
#     return "YES"

def main():
    graph, vertices = create_graph()
    root = '1'
    color = {str(_): 0 for _ in range(1, int(vertices) + 1)}
    visited, color = dfs(graph, root, [], color)
    # print(visited)
    # print(color)
    # print(color)
    # print(bipartite(graph, color))
    print(flag)


if __name__ == '__main__':
    main()
