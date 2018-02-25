# Author: Varun Shijo UB 50244968
# DFS for Graphs


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
    return graph


def bipartite(graph):
    # Traversal
    root = '1'
    current = root
    visited = [current]

    children = [str(_) for _ in sorted(graph[current])]

    while children:
        if str(current) not in visited:
            visited.append(children.pop(0))
        if children:
            current = children[0]


def main():
    graph = create_graph()
    bipartite(graph)


if __name__ == '__main__':
    main()
