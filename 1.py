# Author: Varun Shijo UB 50244968
# DFS for Graphs

vertices, edges = input().split(' ')

graph = {str(_ + 1): [] for _ in range(int(vertices))}

for count in range(int(edges)):
    left, right = input().split(' ')
    if right not in graph[left]:
        graph[left].append(right)
    if left not in graph[right]:
        graph[right].append(left)
