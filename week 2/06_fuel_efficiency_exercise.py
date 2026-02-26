def main():
    # Get input values from the user
    start_miles = float(input("Enter the starting odometer value (miles): "))
    end_miles = float(input("Enter the ending odometer value (miles): "))
    amount_gallons = float(input("Enter the amount of fuel used (gallons): "))

    # Calculate miles per gallon
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    # Convert MPG to liters per 100 kilometers
    lp100k = lp100k_from_mpg(mpg)

    # Display the results
    print(f"Fuel efficiency: {mpg:.2f} miles per gallon")
    print(f"Fuel efficiency: {lp100k:.2f} liters per 100 kilometers")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    """
    miles_traveled = end_miles - start_miles
    mpg = miles_traveled / amount_gallons
    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    """
    lp100k = 235.215 / mpg
    return lp100k


# Call the main function so that
# this program will start executing.
main()
