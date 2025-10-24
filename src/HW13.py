def isLeapYear(year: int) -> str:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "Leap Year"
    else:
        return "Common Year"
year1= int(input())
year2= int(input())

print(isLeapYear(year1))
print(isLeapYear(year2))