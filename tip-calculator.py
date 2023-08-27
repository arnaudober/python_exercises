print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tax = total * (percentage / 100)
split_amount = float((total + tax) / people)
print(f"Each person should pay: ${split_amount:.2f}")
