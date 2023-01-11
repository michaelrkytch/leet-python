from graphutil import topo_sort

edge_s = [[0, 1], [1, 2], [0, 2]]
topo_sort(edge_s)

edge_s = [[0, 1], [1, 0]]
topo_sort(edge_s)


def solution(numCourses, prerequisites):
    sorted_prereqs = topo_sort(prerequisites)
    return sorted_prereqs is not None and numCourses >= len(sorted_prereqs)


print(solution(2, [[1, 0]]))
