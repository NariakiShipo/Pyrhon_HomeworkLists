def split_data(data):
    result = [] 
    temp = []
    for d in data:
        if d == '+':
            result.append(temp)
            temp = []
        else:
            temp.append(d)
    if temp:
        result.append(temp)
    return result

def checkConditionGroup(school_attrs, condition_group, index=0):
    if index >= len(condition_group):
        return True  
    if condition_group[index] not in school_attrs:
        return False
    return checkConditionGroup(school_attrs, condition_group, index + 1)

def checkConditionSingle(school_attrs, condition):
    if condition not in school_attrs:
        return False
    return True
    

def countMatchGroup(school_attrs, query_groups, index=0):
    if index >= len(query_groups):
        return 0
    count = 1 if checkConditionGroup(school_attrs, query_groups[index]) else 0
    return count + countMatchGroup(school_attrs, query_groups, index + 1)

def countMatchSingle(school_attrs, query_groups, index=0):
    if index >= len(query_groups):
        return 0
    count = 0
    for i in range(len(query_groups[index])):
        count += 1 if checkConditionSingle(school_attrs, query_groups[index][i]) else 0
    return count + countMatchSingle(school_attrs, query_groups, index + 1)

def findBestSchol(schools, count):
    school_counts = dict(zip(schools, count))
    sorted_items = sorted(school_counts.items(), key=lambda x: x[1], reverse=True)  
    best_school = max(school_counts.values())
   
    result =[name for name, cnt in sorted_items if cnt == best_school]
    print(' '.join(result))

def countPartialMatch(school_name, count, schools_data, query_groups):
    school_counts = dict(zip(school_name, count))
    
    sorted_items = sorted(school_counts.items(), key=lambda x: x[1], reverse=True)
    result = [name for name, value in sorted_items if value > 0]

    print(' '.join(result))
def main():
    school_num = int(input())
    schools = list()
    school_name = list()
    for i in range(school_num):
        schools.append(input().split())
        school_name.append(schools[i][0])
    
    search_times = int(input())
    search_datas = list()
    for _ in range(search_times):
        text = input().split(" ")
        result = split_data(text)
        search_datas.append(result)
    search_condition = int(input())
    count = []
    for i in range(search_times):
        times = []
        for school in schools:
            if search_condition == 0:
                times.append(countMatchGroup(school, search_datas[i]))
            else:
                times.append(countMatchSingle(school, search_datas[i]))
        count.append(times)
    
    for i in range(search_times):
        if search_condition == 1:
            #print(count[i])
            countPartialMatch(school_name, count[i], schools, search_datas[i])
        else:
            findBestSchol(school_name, count[i])
if __name__ == "__main__":
    main()