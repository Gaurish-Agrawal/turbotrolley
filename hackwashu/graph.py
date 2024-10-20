def create_graph(layout):
    graph = {key: {} for key in layout}
    for key1, coord1 in layout.items():
        for key2, coord2 in layout.items():
            if key1 != key2:
                distance = abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
                graph[key1][key2] = distance
    return graph
