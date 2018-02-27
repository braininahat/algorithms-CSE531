# Author: Varun Shijo UB 50244968
# DFS for Graphs


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


def main():
    graph, vertices = create_graph()
    print(graph)


if __name__ == '__main__':
    main()
