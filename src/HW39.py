def next_cave(caves_info, bag_weight_limit, current_weight , current_value, cave_id , visited = None):
    #Base Case
    if visited is None:
        visited = set()
    if cave_id == 0 or cave_id in visited:
        return current_value
    
    _ , val, weight, cave_1, cave_2 = caves_info[cave_id - 1]
    if current_weight + weight >= bag_weight_limit:
        return current_value
    if val == 0:
        return current_value
    visited.add(cave_id)
    #Recursive Case
    original_value = current_value
    original_weight = current_weight
    current_value += val
    current_weight += weight
   
    if cave_1 == 0 or cave_2 == 0:
        return current_value

    value_1 = next_cave(caves_info, bag_weight_limit, current_weight, current_value,cave_1)
    value_2 = next_cave(caves_info, bag_weight_limit, current_weight, current_value,cave_2)
    current_value = original_value
    current_weight = original_weight
    return max(value_1, value_2)
def explore_caves(caves_info, first_cave, bag_weight_limit):
    _ , val, weight, cave_1, cave_2 = caves_info[first_cave - 1]

    # 為 Y 分支創建獨立的 visited set
    visited1 = set()
    visited1.add(first_cave)
    first_value = next_cave(caves_info, bag_weight_limit, weight, val, cave_1, visited1)
    
    # 為 Z 分支創建獨立的 visited set
    visited2 = set()
    visited2.add(first_cave)
    second_value = next_cave(caves_info, bag_weight_limit, weight, val, cave_2, visited2)
    
    max_value = max(first_value, second_value)
    
    return max_value
def main():
    cave_counts , first_cave = map(int, input().split())
    bag_weight_limit = int(input())
    caves_info = list() #caves_info[0] = cave_number,caves_info[1] = gold_value,caves_info[2] = gold_weight,
    #caves_info[3,4]=next cave
    for _ in range (cave_counts):
        data = [int(x) for x in input().split()]
        caves_info.append(data)
        
    value = explore_caves(caves_info, first_cave, bag_weight_limit)
    print(value)
if __name__ == "__main__":
    main()