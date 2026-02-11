#Example 1:

import math
def print_cylinder_volume():
    """Compute the volume of a cylinder"""
    # Get the radius and height from the user.
    radius = float(input("Enter the radius of a cylinder: "))
    height = float(input("Enter the height of a cylinder: "))
  # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height
    # Print the volume of the cylinder.
    print(f"Volume: {volume:.2f}")

# Because the print_cylinder_volume function in example 1 doesn’t accept parameters, it must be called without any arguments
print_cylinder_volume()




# Example 2:
# How to Make a User-Defined Function Reusable: 
# The most reusable functions are ones that take parameters, perform calculations, and return a result but do not perform user input and output. A parameter is a variable whose value comes from outside the function. 

import math
# Define a function named print_cylinder_volume.
def print_cylinder_volume(radius, height):
  """Compute and print the volume of a cylinder.
  Parameters
  radius: the radius of the cylinder
  height: the height of the cylinder
  Return: nothing
  """
  # Compute the volume of the cylinder.
  volume = math.pi * radius**2 * height
  # Print the volume of the cylinder.
  print(volume)

# Because the second version of the print_cylinder_volume function accepts two parameters, it must be called with two arguments like this:
print_cylinder_volume(2, 10)



# Example 3:
# Notice that the version in example 3 returns the volume instead of printing it, which makes the function more reusable.

import math
# Define a function named computer_cylinder_volume.
def compute_cylinder_volume(radius, height):
  """Compute and return the volume of a cylinder.
  Parameters
  radius: the radius of the cylinder
  height: the height of the cylinder
  Return: the volume of the cylinder
  """
  # Compute the volume of the cylinder.
  volume = math.pi * radius**2 * height
  # Return the volume of the cylinder so that the
  # volume can be used somewhere else in the program.
  return volume

# Because the compute_cylinder_volume function in example 3 accepts two parameters and returns a result, it could be called like this:

volume = compute_cylinder_volume(2.5, 4.1)
print(volume)




# Example 6
import math
# Define the main function.
def main():
  # Get a radius and a height from the user.
  radius = float(input("Enter the radius of a cylinder: "))
  height = float(input("Enter the height of a cylinder: "))
  # Call the compute_cylinder_volume function and store
  # its return value in a variable to use later.
  volume = compute_cylinder_volume(radius, height)
  # Print the volume of the cylinder.
  print(f"Volume: {volume:.2f}")
# Define a function that accepts two parameters.


def compute_cylinder_volume(radius, height):
  """Compute and print the volume of a cylinder.
  Parameters
  radius: the radius of the cylinder
  height: the height of the cylinder
  Return: the volume of the cylinder
  """
  # Compute the volume of the cylinder.
  volume = math.pi * radius**2 * height
  # Return the volume of the cylinder so that the
  # volume can be used somewhere else in the program.
  # The returned result will be available wherever
  # this function was called.
  return volume
# Start this program by
# calling the main function.
main()

# NOTE: The most reusable functions are ones that have parameters, perform calculations, and return a result but do not perform user input and output.

# The main function is certainly useful in the program, but it is not reusable in other programs because it gets user input and prints the result for the user to see. The compute_cylinder_volume function is very reusable in another program because it doesn’t get user input or print output. Instead, it takes two parameters, performs a calculation, and returns a result to the calling function.