import math

Name = ['A', 'B', 'C']
Prices = [380, 1200, 180]
Discounts = []
Count = []
for i in range(3):
    inputs = list(map(int, input().split()))
    Count.append(inputs[0]) 
    Discounts.append(inputs[1:])

total = []

for i in range(3):
    if Count[i] > 30:
        total.append(math.ceil(Prices[i] * (Discounts[i][2] / 100) * Count[i])) 
    elif Count[i] > 20:
        total.append(math.ceil(Prices[i] * (Discounts[i][1] / 100) * Count[i]))
    elif Count[i] > 10:
        total.append(math.ceil(Prices[i] * (Discounts[i][0] / 100) * Count[i]))
    else:
        total.append(Prices[i] * Count[i])

max_total_num = 0
min_total_num = 0
for i in range(3):
    if total[i] == max(total):
        max_total_num = i
    if total[i] == min(total):
        min_total_num = i
print(f"{Name[max_total_num]}: {total[max_total_num]}")
print(f"{Name[min_total_num]}: {total[min_total_num]}")
print(sum(total))

