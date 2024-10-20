import heapq
from store_layout import find_store
from graph import create_graph
from dijkstra import dijkstra
from itertools import permutations
from draw_path import draw

def get_pairwise_distances(graph, nodes):
    pairwise_distances = {}
    for node in nodes:
        distances, _ = dijkstra(graph, node)
        pairwise_distances[node] = distances
    return pairwise_distances

def get_optimized_path(items, address):
    
    store_layout = find_store(address)
    graph = create_graph(store_layout)
    start = 'Entrance'
    end = 'Checkout'

    # Extract sections from the items dictionary
    sections = sorted(set(items.keys()))  # Sort sections to ensure deterministic order
    all_nodes = [start] + sections + [end]

    # Generate pairwise distances
    pairwise_distances = get_pairwise_distances(graph, all_nodes)


    # Create a function to get the total distance of a path
    def path_distance(path):
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += pairwise_distances[path[i]][path[i+1]]
        return total_distance

    # Generate all possible paths visiting all sections
    possible_paths = permutations(sections)
    
    # Find the shortest path
    shortest_path = None
    min_distance = float('infinity')
    for perm in possible_paths:
        current_path = [start] + list(perm) + [end]
        current_distance = path_distance(current_path)
        if current_distance < min_distance:
            shortest_path = current_path
            min_distance = current_distance

    return shortest_path, min_distance

if __name__ == "__main__":

    items = {
    'Garden': [
        {'item': 'plant', 'quantity': 6}
    ],
    'Health & Wellness': [
        {'item': 'toothpaste', 'quantity': 3}
    ],
    'Storage & Laundry': [
        {'item': 'storage bins', 'quantity': 4}
    ],
    }

    path, distance = get_optimized_path(items)
    print("Optimized Path:", path) 

    image_path = '/Users/gaurishagrawal/Downloads/IMG_5119.jpg'
    draw(path, image_path)
    print("Done")