
age = input("What is your current age?: ")

day = 365 * 90
week = 52 * 90
month = 12 * 90

age_day = int(age) * 365
age_week = int(age) * 52
age_month = int(age) * 12

print(f"You have {day - age_day} days, {week - age_week} weeks, and {month - age_month} months left. ")
