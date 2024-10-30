# Leap year code in Python using for loop
# Added comment For Testing
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Get input from the user
start_year = int(input("Enter the starting year: "));
end_year = int(input("Enter the ending year: "));
start_year = int(input("Enter the starting year: "));

# Check leap year for each year in the range
for year in range(start_year, end_year + 1):
    if is_leap_year(year):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")