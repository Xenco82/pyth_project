# python project
This is a repository created for the purpose of building my portfolio of Python projects.

# band_name_generator

 ``` python

#1. Create a greeting for your program.
print("Hello? it is good program!")
#2. Ask the user for the city that they grew up in.
city = input("where is your in the city?: \n")
# 3. Ask the user for the name of a pet.
pet = input("where is your pet name?: \n")
#4. Combine the name of their city and pet and show them their band name.
print (("your band name is..") + (city +(" ")+ pet))
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end

```

# Tip_calcurator

``` python
print                   ("Welcome to the tip calculator!")
totall_bill     =  input("What was the total bill? $")
How_much_tip    = input("How much tip would you like to give? 10, 12, or 15? ")
How_many_people = input("How many people to split the bill? ")

bill  = float(totall_bill)
c_tip = int(How_much_tip) * 0.01
people = int(How_many_people) 

percentage = bill * c_tip
last_percentage = bill + percentage

last_tip = last_percentage / people
tip = round(last_tip, 2)


print(f"Each person should pay: ${tip}")
```

# have_life
```python
age = input("What is your current age?: ")

day = 365 * 90
week = 52 * 90
month = 12 * 90

age_day = int(age) * 365
age_week = int(age) * 52
age_month = int(age) * 12

print(f"You have {day - age_day} days, {week - age_week} weeks, and {month - age_month} months left. ")

#print(f"You have 12410 days", "1768 weeks", "and 408 months left.")
```

