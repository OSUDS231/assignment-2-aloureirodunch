# Getting inputs for the three variables

initial_height = int(input("Enter the plant's initial height in cm: "))

daily_growth = float(input("Enter the daily growth rate as a proportion: "))

days = int(input("Enter the number of days to simulate: "))

# for loop to calculate the final height of the plant with a print function to report height each day

for i in range(days):
    initial_height += (initial_height * daily_growth)
    if (i==0):
        print(f"After 1 day, the plant is {initial_height} cm tall.")
    else:
        print(f"After {i + 1} days, the plant is {initial_height} cm tall.")