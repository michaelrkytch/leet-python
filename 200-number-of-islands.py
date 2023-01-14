from typing import List, Tuple

from graphutil import bfs


def convert_grid(grid: List[List[str]]) -> None:
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            grid[row][col] = int(grid[row][col])


# Return the children of a node in the 2d grid --
# nodes that are vertically or horizontally adacent to v,
# are within the bounds of the graph, and have values > 0
def childrenfn(v: Tuple[int, int], graph):
    maxrow = len(graph)
    maxcol = len(graph[0])
    row = v[0]
    col = v[1]
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

    return [n for n in neighbors
            if 0 <= n[0] < maxrow and 0 <= n[1] < maxcol
            and graph[n[0]][n[1]] > 0]


# Iterate through matrix, and for any node that hasn't yet been visited and is non-zero
#  start a tree search from that node to discover all connected non-zero nodes
#  keeping a count of the disjoint trees that have been discovered
def solution(graph):
    maxrow = len(graph)
    maxcol = len(graph[0])
    visited = set()
    n = 0

    for row in range(maxrow):
        for col in range(maxcol):
            if (row, col) not in visited and graph[row][col] > 0:
                n += 1
                visited.add((row, col))
                for node in bfs(graph, childrenfn, (row, col)):
                    visited.add(node)

    return n

