# Author: Varun Shijo UB 50244968
# DFS for Graphs


def create_graph(vertices, edges):
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


def bipartite(graph, vertices):
    root = '1'
    stack = [root]
    visited = [0 for _ in range(int(vertices))]
    head = 1
    while head >= 1:
        head -= 1
        current = stack[head]
        if not visited[head]:
            visited[head] = 1
            neighbors = graph[current]
            for neighbor in neighbors:
                if not visited[int(neighbor) - 1]:
                    head += 1
                    stack.insert(head,neighbor)


def main():
    vertices, edges = input().split(' ')
    graph = create_graph(vertices, edges)
    bipartite(graph, vertices)


if __name__ == '__main__':
    main()
