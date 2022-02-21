from dynamic.wis.wis import weighted_independent_set


def test_wis_1():
    weighted_path_graph = [5, 3, 1, 7, 2, 4, 6]
    wis_cost = 18
    node_list = (0, 3, 6)

    assert weighted_independent_set(weighted_path_graph) == (wis_cost, node_list)

    weighted_path_graph = [3, 2, 1, 6, 4, 5]
    wis_cost = 14
    node_list = (0, 3, 5)

    assert weighted_independent_set(weighted_path_graph) == (wis_cost, node_list)

    weighted_path_graph = [5, 3]
    wis_cost = 5
    node_list = (0,)

    assert weighted_independent_set(weighted_path_graph) == (wis_cost, node_list)

    weighted_path_graph = [5, 8, 1]
    wis_cost = 8
    node_list = (1,)

    assert weighted_independent_set(weighted_path_graph) == (wis_cost, node_list)
