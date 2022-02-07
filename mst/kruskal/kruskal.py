###############################################################################################################
# Programming problem 15.9. Algorithms Illuminated. Part 2 by Tim Roughgarden
###############################################################################################################

from typing import List, Union, Iterable


class UnionFind:
    """
    TODO add description
    """
    def __init__(self, node_list: Iterable[Union[str, int]]):
        self.area_map = {node: node for node in node_list}

    def is_same_root(self, node_a: Union[str, int], node_b: Union[str, int]) -> bool:
        root_a, _ = self.get_root(node_a)
        root_b, _ = self.get_root(node_b)
        return root_a == root_b

    def union(self, node_a: Union[str, int], node_b: Union[str, int]) -> Union[str, int]:
        root_a, depth_a = self.get_root(node_a)
        root_b, depth_b = self.get_root(node_b)

        if root_a == root_b:
            return root_a

        if depth_a < depth_b:
            self.area_map[root_a] = root_b
        else:
            self.area_map[root_b] = root_a

    def get_root(self, node: Union[str, int]) -> (Union[str, int], int):
        root_depth = 0
        node_current = node
        while node_current != self.area_map[node_current]:
            node_current = self.area_map[node_current]
            root_depth += 1
        return node_current, root_depth


def mst_kruskal_basic(edge_list: List[tuple]) -> list:
    """
    TODO add description
    :param edge_list: list of graph edges with every item as tuple (edge_cost, vertex_a, vertex_b)
    :param start_vertex: start vertex id
    :return: mst as list of edges
    """
    el = edge_list.copy()
    el = sorted(el, key=lambda x: x[0])  # a crucial thing for fast MST construction

    uf = UnionFind(set([x for item in edge_list for x in item[1:]]))

    mst_edge_list = []

    for cost, v_a, v_b in el:
        if not uf.is_same_root(v_a, v_b):
            uf.union(v_a, v_b)
            mst_edge_list.append((cost, v_a, v_b))

    return mst_edge_list


