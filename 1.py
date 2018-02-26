# Author: Varun Shijo UB 50244968
# DFS for Graphs

flag = "YES"


def create_graph():
    vertices, edges = input().split(' ')

    # dictionary comprehension to initialize graph nodes
    graph = {str(_ + 1): [] for _ in range(int(vertices))}
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
        color[int(current)] = 1 - color[int(current)-1]
        for neighbor in neighbors:
            dfs(graph, neighbor, visited, color)
    elif color[int(current)] == color[int(current) - 1]:
        flag = "NO"
    return visited, color


def main():
    graph, vertices = create_graph()
    root = '1'
    color = [0 for _ in range(int(vertices) + 1)]
    visited, color = dfs(graph, root, [], color)
    print(visited)
    print(color)
    print(flag)


if __name__ == '__main__':
    main()
