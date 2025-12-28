def canAssign(cargo, carCount, cargoLimit):
    weight = sorted(calculateSumWeight(cargo), reverse=True)
    total_weight = sum(weight)
    
    # 檢查總重量能否被車廂數整除
    if total_weight % carCount != 0:
        return False
    
    eachWeight = total_weight // carCount
    buckets = [[0, 0] for _ in range(carCount)]
    if canDistribute(weight, buckets, target_weight=eachWeight, max_count=cargoLimit):
        return True
    return False
def canDistribute(cargo, buckets, index=0, target_weight=0, max_count=0):
    # Base Case 
    if index >= len(cargo):
        # 檢查所有車廂是否都達到目標重量
        return all(bucket[0] == target_weight for bucket in buckets)
    
    # 當前貨物的重量
    weight = cargo[index]
    
    # Recursive case: 嘗試每個車廂
    for i in range(len(buckets)):
        # 剪枝條件1: 重量超標
        if buckets[i][0] + weight > target_weight:
            continue
        
        # 剪枝條件2: 數量超標
        if buckets[i][1] >= max_count:
            continue
        
        # 剪枝條件3: 對稱性剪枝 - 避免嘗試等價的空車廂
        if i > 0 and buckets[i][0] == 0 and buckets[i-1][0] == 0:
            break
        
        # 剪枝條件4: 如果當前貨物放入後，車廂已滿但未達到目標重量，且剩餘貨物無法填滿
        if buckets[i][0] + weight < target_weight and buckets[i][1] + 1 >= max_count:
            # 車廂將滿但重量不足，檢查是否還有足夠貨物
            remaining_weight = target_weight - buckets[i][0] - weight
            remaining_space = max_count - buckets[i][1] - 1
            if remaining_space == 0 and remaining_weight > 0:
                continue
        
        # 放入車廂
        buckets[i][0] += weight
        buckets[i][1] += 1
        
        # 遞迴
        if canDistribute(cargo, buckets, index + 1, target_weight, max_count):
            return True
        
        # 回溯
        buckets[i][0] -= weight
        buckets[i][1] -= 1
        
        # 剪枝條件5: 如果放入第一個空車廂失敗，不用再試其他空車廂
        if buckets[i][0] == 0:
            break
    
    return False


def calculateSumWeight(cargo):
    cargoDict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    count = []
    for c in cargo:
        count.append(cargoDict[c])  
    return count
def main():
    cargo = input()
    carCount = int(input())
    cargoLimit =int(input())
    
    # error 條件：字母不在 A-Z、字串長度超過 50、或總貨物數超過總容量
    #or len(cargo) > carCount * cargoLimit
    if not(cargo.isalpha() and cargo.isupper()) or len(cargo) > 50:
        print("error")
        return
    if canAssign(cargo, carCount, cargoLimit):
        print("ok")
    else:
        print("fail")
if __name__ == "__main__":
    main()