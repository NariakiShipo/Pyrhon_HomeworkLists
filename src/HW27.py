
#print the garden status
def check_garden(garden_grid: list):
    if garden_grid is None:
        return garden_grid
    for i in range(5):
        for j in range(5):
            print(garden_grid[i][j], end=' ')
        print()
def change_status(plant_grid: list) -> list:
    if plant_grid is None:
        return plant_grid
    canChange = [[True]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if plant_grid[i][j] == "__":
                continue
            elif canChange[i][j] == False:
                continue
            elif plant_grid[i][j] == "Ai" and canChange[i][j]:
                for k in range(5):
                    if plant_grid[i][k] != "__" and k != j:
                        plant_grid[i][j] = "Cn"
                        canChange[i][j] = False
                        break
            elif plant_grid[i][j] == "Cn" and canChange[i][j]:
                if i - 1 >= 0 and plant_grid[i - 1][j] != "__":
                        plant_grid[i][j] = "Hy"
                        canChange[i][j] = False
            elif plant_grid[i][j] == "Hy" and canChange[i][j]:
                isPlanted = 0

                if j-1 >= 0 and plant_grid[i][j-1] != "__":
                    isPlanted += 1
                if j+1 < 5 and plant_grid[i][j+1] != "__":
                    isPlanted += 1
                if i-1 >= 0 and plant_grid[i-1][j] != "__":
                    isPlanted += 1
                if i+1 < 5 and plant_grid[i+1][j] != "__":
                    isPlanted += 1

                if isPlanted >= 2:
                    if j-1 >= 0 and plant_grid[i][j-1] == "__":
                        canChange[i][j-1] = False
                        plant_grid[i][j-1] = "Na"
                    if j+1 < 5 and plant_grid[i][j+1] == "__":
                        canChange[i][j+1] = False
                        plant_grid[i][j+1] = "Na"
                    if i-1 >= 0 and plant_grid[i-1][j] == "__":
                        plant_grid[i-1][j] = "Na"
                        canChange[i-1][j] = False
                    if i+1 < 5 and plant_grid[i+1][j] == "__":
                        plant_grid[i+1][j] = "Na"
                        canChange[i+1][j] = False
                
            elif plant_grid[i][j] == "Na" and canChange[i][j]:
                if j+1 < 5 and plant_grid[i][j+1] == "__":
                    plant_grid[i][j+1] = "Qx"
                    canChange[i][j+1] = False

                if j-1 >= 0:
                    plant_grid[i][j-1] = "Hy"
                    canChange[i][j-1] = False

            elif plant_grid[i][j] == "Qx" and canChange[i][j]:
                samePlant = {}
                for k in range(5):
                    if plant_grid[i][k] != "__":
                        if plant_grid[i][k] in samePlant:
                            samePlant[plant_grid[i][k]] += 1
                        else:
                            samePlant[plant_grid[i][k]] = 1
                for plant, num in samePlant.items():
                    if num >= 3:
                        for r in range(5):
                            if plant_grid[i][r] == plant:
                                plant_grid[i][r] = "Ai"
                                canChange[i][r] = False
                        break
    return plant_grid
def main():
    days = int(input())
    gardens = []
    for _ in range(5):
        space = input().split()
        gardens.append(space)

    while days > 0:
        gardens = change_status(gardens)
        # check_garden(gardens)
        # print()
        days -= 1
    check_garden(gardens)
main()