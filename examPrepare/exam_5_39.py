
def next_cave(caves_info, bag_weight_limit, current_weight, current_value, cave_id, visited=None):
    #base case
    if visited is None:
        visited = set()
    if cave_id == 0 or cave_id in visited:
        return current_value
    
    _ , val, weight, cave_1, cave_2 = caves_info[cave_id]
    if current_weight + weight > bag_weight_limit:
        return current_value
    
    # 加上當前洞穴的金值和重量
    current_value += val
    current_weight += weight
    
    visited_new = visited.copy()
    visited_new.add(cave_id)
    
    # 檢查是否為葉子節點
    if cave_1 == 0 and cave_2 == 0:
        return current_value
    
    #recursive case - 為每個分支創建獨立的 visited 副本
    value_1 = next_cave(caves_info, bag_weight_limit, current_weight, current_value, cave_1, visited_new)
    value_2 = next_cave(caves_info, bag_weight_limit, current_weight, current_value, cave_2, visited_new)

    return max(value_1, value_2)

    
    
def explore_caves(caves_info, first_cave, bag_weight_limit):
    
    _ , val, weight, cave_1, cave_2 = caves_info[first_cave]  # 用字典訪問

    visited1 = set()
    visited1.add(first_cave)
    first_value = next_cave(caves_info, bag_weight_limit, weight, val, cave_1, visited1)
    
    visited2 = set()
    visited2.add(first_cave)
    second_value = next_cave(caves_info, bag_weight_limit, weight, val, cave_2, visited2)
    
    return max(first_value, second_value)


def main():
    cave_count, first_cave = map(int, input().split())
    bag_weight_limit = int(input())
    caves_info = {}  # 用字典而不是列表
    for _ in range(cave_count):
        data = [int(x) for x in input().split()]
        cave_num = data[0]
        caves_info[cave_num] = data
    value = explore_caves(caves_info, first_cave, bag_weight_limit)
    print(value)

if __name__ == "__main__":
    main()