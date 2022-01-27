
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
