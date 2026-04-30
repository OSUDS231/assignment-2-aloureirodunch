# get 5 input variables from the user

initial_height = float(input("Enter the initial height of the plant in cm: "))
daily_growth = float(input("Enter the daily growth rate as a proportion: "))
days = int(input("Enter the number of days to simulate for: "))
target_height = float(input("Enter the desired height to reach in cm: "))
boost_amount = float(input("Enter the number of cm the plant is boosted by each time a boost is applied: "))

#define some variables we'll use for our logic
boost_frequency = 0
no_boost_height = initial_height

#Calculating the height the plant gets to with no boosts
for i in range(days):
    no_boost_height += (no_boost_height * daily_growth)

#Checking if any boosts are actually needed
if no_boost_height >= target_height:
    print("No boosts are needed!")
else:

    #determining how much extra height is necessary
    height_defecit = target_height - no_boost_height

    #calculating the amount of boosts needed
    boosts_needed = height_defecit / boost_amount

    #calculating frequency
    boost_frequency = int(days/boosts_needed)

    #Print results!
    print(f"To reach at least {target_height} cm in {days} days, apply a {boost_amount} cm boost every {boost_frequency} days.")