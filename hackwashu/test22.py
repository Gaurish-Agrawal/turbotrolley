import heapq
from draw_path import draw

# Define a class to represent nodes in the grid
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.g = float('inf')  # Cost from start node to this node
        self.h = float('inf')  # Heuristic (estimated cost from this node to end node)
    
    def __lt__(self, other):
        # Required for priority queue comparison
        return (self.g + self.h) < (other.g + other.h)

def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def is_valid(node, obstacles):
    if 0 <= node.x < 1165 and 0 <= node.y < 793:
        for obstacle in obstacles:
            bottomLeft = obstacle[0]  # Bottom-left corner
            bottomRight = obstacle[1]  # Bottom-right corner
            topRight = obstacle[2]  # Top-right corner
            topLeft = obstacle[3]  # Top-right corner



            if node.x in range(bottomLeft[0], bottomRight[0]) and node.y in range(topLeft[1],bottomLeft[1]):
                return False  # Node is inside an obstacle box
        
        
        return True  # Node is not inside any obstacle box
    return False  # Node is outside the grid

# Find the shortest path using A*
def astar(start, goal, obstacles):
    open_set = []
    closed_set = set()
    
    start_node = Node(start[0], start[1])
    start_node.g = 0
    start_node.h = heuristic(start_node, Node(goal[0], goal[1]))
    
    heapq.heappush(open_set, start_node)
    
    while open_set:
        current = heapq.heappop(open_set)
        
        if (current.x, current.y) == goal:
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            path.reverse()
            return combine_points(path)
        
        closed_set.add((current.x, current.y))
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_node = Node(current.x + dx, current.y + dy)
            
            if is_valid(next_node, obstacles) and (next_node.x, next_node.y) not in closed_set:
                tentative_g = current.g + 1  # Assuming uniform cost
                
                if tentative_g < next_node.g:
                    next_node.parent = current
                    next_node.g = tentative_g
                    next_node.h = heuristic(next_node, Node(goal[0], goal[1]))
                    heapq.heappush(open_set, next_node)
    
    return None  # No path found

def combine_points(path):
    if len(path) < 3:
        return path
    combined_path = [path[0]]
    for i in range(1, len(path) - 1):
        x1, y1 = combined_path[-1]
        x2, y2 = path[i]
        x3, y3 = path[i + 1]
        if (x1 == x2 == x3) or (y1 == y2 == y3):
            continue
        combined_path.append((x2, y2))
    combined_path.append(path[-1])
    return combined_path


# Example usage
start = (1165, 93)
goal = (281,86)
goal2 = (1088,247)
goal3 = (98,791)

obstacles = [
    [(122, 275), (1044, 275), (1034, 101), (137, 101)],
    [(113,447), (901,446), (892,289), (126,284)],
    [(123,640), (900,640), (900,475), (123,475)],
    [(114,835),(898,835),(900,675),(123,675)],
    [(123,943),(896,943),(890,872),(126,872)],
    [(64,77),(1032,77),(1032,0),(64,0)],
    [(0,780),(75,780),(75,5),(0,0)],

] 

path = astar(start, goal, obstacles)+astar(goal, goal2,obstacles)+astar(goal2, goal3,obstacles)
print(path)
#['Entrance', 'Frozen', 'Checkout']

address = "2850 Quimby Rd, San Jose, CA"
image_path = "static/"+address.replace(" ","").replace(",","")+".png" #reuse

new_path = "static/newimage.png"

draw(path, image_path, new_path, address)