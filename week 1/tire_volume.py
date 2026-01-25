#importing the needed modules/libraries

import math
from datetime import datetime

# user input
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# volume calculation
volume = (
    math.pi * (width ** 2) * aspect_ratio *
    (width * aspect_ratio + 2540 * diameter)
) / 10_000_000_000

# Display the result
print(f"\nThe approximate volume is {volume:.2f} liters")
100

# an if condition to update the user if they needed to refill the tire. 
print ("warning⛔⛔⛔:You need to refil you tyre\n".upper()) if volume<=10 else print("🚦🚦🚦your tyre is in a good condition\n".upper())

# current date using the datetime module
current_date = datetime.now().date()

# Append the data to volumes.txt
with open("volumes.txt", "at") as volume_file:
    print(
        f"{current_date}, {int(width)}, {int(aspect_ratio)}, {int(diameter)}, {volume:.2f}",
        file=volume_file
    )
