#collect input from the user for 4 variables

initial_height = int(input("Enter the initial height of the plant in cm: "))
daily_growth = float(input("Enter the daily growth rate as a proportion: "))
days = int(input("Enter the number of days to simulate for: "))
boost_amount = int(input("Enter the number of cm the plant is boosted by every 7th day: "))

#for loop to determine the final height and print results for each day

for i in range(days):
    initial_height += (initial_height * daily_growth)
    if (i+1) % 7 == 0:
        initial_height += boost_amount
    if(i==0):
        print(f"After 1 day (with a {boost_amount} cm boost every 7th day), the plant is {initial_height} cm tall.")
    else:
        print(f"After {i+1} days (with a {boost_amount} cm boost every 7th day), the plant is {initial_height} cm tall.")