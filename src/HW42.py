from collections import deque

def bfs(graph, start, end):
    
    if start == end:
        return [start]
        
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        current_node, path = queue.popleft()
        
        if current_node in graph:
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    if neighbor == end:
                        return new_path
                    queue.append((neighbor, new_path))
    return None

def solve():
    """
    Reads one full test case, solves it, and prints the output.
    Raises EOFError if input ends.
    """
    line1 = input()
    if not line1.strip():  # Handles blank lines between test cases
        return

    n_str, start_node_str, end_node_str = line1.split()
    n = int(n_str)
    start_node = int(start_node_str)
    end_node = int(end_node_str)
    
    rest_stops_str = input().split()
    rest_stops = sorted([int(rs) for rs in rest_stops_str])
    
    graph = {}
    for _ in range(n):
        a_str, b_str = input().split()
        a, b = int(a_str), int(b_str)
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    shortest_path = None
    min_length = float('inf')
    best_rest_stop = -1

    for stop in rest_stops:
        path1 = bfs(graph, start_node, stop)
        path2 = bfs(graph, stop, end_node)
        
        if path1 and path2:
            combined_path = path1[:-1] + path2
            current_length = len(combined_path)
            
            if current_length < min_length:
                min_length = current_length
                shortest_path = combined_path
                best_rest_stop = stop
    
    if shortest_path:
        print(best_rest_stop)
        print(*shortest_path)
    else:
        print("NO")

if __name__ == "__main__":
    while True:
        try:
            solve()
        except EOFError:
            break
        except (IOError, ValueError):
            break
