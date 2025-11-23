def calConfirm(days: int, people : int,first_confirmed: int, infect: float, rehabiliatatioDays : int, immunity: float):
    day_confirmed = first_confirmed
    new_confirmed = first_confirmed
    day_rehabiliatation = 0
    confirmList = [day_confirmed]
    all_confirmed = new_confirmed
    j = 0
    
    
    for i in range(1, days+1):
        print(f'{i} {day_confirmed} {new_confirmed} {day_rehabiliatation}')
        
        susceptible = int(people * (1 - immunity)) - day_confirmed
        if susceptible < 0:
            susceptible = 0
        calConfirmRate = (infect / rehabiliatatioDays)* (1 - immunity)
        
        new_confirmed = int(day_confirmed * calConfirmRate)
        
        
        if new_confirmed > susceptible : new_confirmed = susceptible
        
        if (i < days):
            day_confirmed+= new_confirmed
            all_confirmed += new_confirmed
        confirmList.append(new_confirmed)
        if(i >= rehabiliatatioDays):
            if j > len(confirmList): break
            day_confirmed -= confirmList[j]
            immunity = immunity + (confirmList[j] / people)
            day_rehabiliatation = confirmList[j]
            if first_confirmed < 0: first_confirmed = 0
            j += 1
    print(all_confirmed)

def main():
    people = int(input())
    days = int(input())
    first_confirmed = int(input())
    infect = float(input())
    rehabiliatationDays = int(input())
    immunity = float(input())

    calConfirm(days , people , first_confirmed, infect, rehabiliatationDays, immunity)

if __name__ == "__main__":
    main()