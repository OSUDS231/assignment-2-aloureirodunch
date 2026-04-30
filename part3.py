# collect 4 input variables

initial_height = int(input("Enter the initial height of the plant in cm: "))
daily_growth = float(input("Enter the daily growth rate as a proportion: "))
target_height = int(input("Enter the desired height to reach in cm: "))
boost_amount = int(input("Enter the number of cm the plant is boosted by every 7th day: "))

days_needed = 0

# while loop to determine the amount of days needed
while initial_height <= target_height:
    days_needed += 1
    initial_height += (initial_height * daily_growth)
    if (days_needed + 1) % 7 == 0:
        initial_height += boost_amount

#print the result for the user to see
print(f"After {days_needed} days (with a {boost_amount} cm boost every 7th day), the plant reaches at least {target_height} cm.")
