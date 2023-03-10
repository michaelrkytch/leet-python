from collections import defaultdict, deque
from typing import Tuple, Any, List, Dict


def _edge_map(edges: List[Tuple[Any, Any]]) -> Dict[Any, set]:
    m = defaultdict(set)
    for v1, v2 in edges:
        m[v1].add(v2)
    return m


def _indegrees(edges: List[Tuple[Any, Any]]) -> Dict[Any, int]:
    m = defaultdict(int)
    for v1, v2 in edges:
        m[v1] = 0
    for v1, v2 in edges:
        m[v2] += 1
    return m


def _find_root(indegrees: Dict[Any, int]) -> Any:
    for item in indegrees.items():
        if item[1] == 0:
            return item[0]
    return None


def _remove_root(indegrees: Dict[Any, int], edge_map: Dict[Any, set], node: Any) -> None:
    # Decrement the count of the nodes neighbors
    neighbors = edge_map[node]
    for v in neighbors:
        indegrees[v] -= 1
    # remove node
    del indegrees[node]


def topo_sort(edges: List[Tuple[Any, Any]]) -> List[Any]:
    edge_map = _edge_map(edges)
    indegrees = _indegrees(edges)
    next_root = _find_root(indegrees)
    path = []
    while next_root is not None:
        path.append(next_root)
        _remove_root(indegrees, edge_map, next_root)
        next_root = _find_root(indegrees)
    if len(indegrees) == 0:
        return path
    else:
        return None


# Traverse graph from the given root breadth-first.
# Produces the (lazy) sequence of nodes visited
# childrenfn [v graph] returns the neihbors of v in graph
# Graph representation can be anything that supports childrenfn
def bfs(graph, childrenfn, root) -> List:
    visitqueue = deque()
    visitqueue.append(root) # Not using constructor b/c that seems to flatten collections
    visited = {root}

    while visitqueue:
        yield (node := visitqueue.popleft())
        # Put neighbors on the queue to visit later
        for v in childrenfn(node, graph):
            if v not in visited:
                visited.add(v)
                visitqueue.append(v)
