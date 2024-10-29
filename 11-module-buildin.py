# importing built-in module math
import math

# using square root(sqrt) function contained 
# in math module
print("SQRT(25) : ", math.sqrt(25)) 

# using pi function contained in math module
print("Value of Pi : ", math.pi) 

# 1 * 2 * 3 * 4 = 24
print("Factorial of 4 : ", math.factorial(4)) 

# importing built in module random
import random

# printing random integer between 0 and 5
print("Random int between 0 and 5 : ", random.randint(0, 5)) 

# random number between 0 and 100
print("Random number between 0 and 100 : ", random.random() * 100) 

List = [13, 40, True, "world", 78, "python", 207, "hello"]

# using choice function in random module for choosing 
# a random element from a set such as a list
print("Random choice from the list [13, 40, True, world, 78, python, 207, hello] : ", random.choice(List)) 


# importing built in module datetime
from datetime import date
from datetime import datetime

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)