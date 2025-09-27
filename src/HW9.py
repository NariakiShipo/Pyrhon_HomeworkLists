x1_coordinate = list()
x2_coordinate = list()

for i in range(3):
    x1, x2 = int(input()), int(input())
    if -20 < x1 < 20 and -20 < x2 < 20:
        ValueError("Out of range") 
    x1_coordinate.append(x1)
    x2_coordinate.append(x2)

start_point = x1_coordinate[0]
end_point = x2_coordinate[0]
sum = 0
for i in range(3):
    if  start_point < x2_coordinate[i] < end_point and x1_coordinate[i] < start_point:
        start_point = x1_coordinate[i]
    if start_point < x1_coordinate[i] < end_point and x2_coordinate[i] > end_point:
        end_point = x2_coordinate[i]
    if x1_coordinate[i] > end_point or x2_coordinate[i] < start_point:
        sum += abs(x2_coordinate[i] - x1_coordinate[i])
sum += abs(end_point - start_point)
print(sum)

    