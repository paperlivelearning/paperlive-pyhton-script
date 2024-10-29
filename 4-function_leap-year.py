# Check leap year in Python using python function

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Get input from the user
year = int(input("Enter a year : "))

# Call the function and check if it's a leap year
if is_leap_year(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")