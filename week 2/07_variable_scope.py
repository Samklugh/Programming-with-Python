# The scope of a variable determines how long that variable exists and where it can be used. Within a Python program, there are two categories of scope: local and global. A variable has local scope when it is defined (assigned a value) inside a function. A variable has global scope when it is defined outside of all functions.

# g is a global variable because it
# is defined outside of all functions.
g = 25
def main():
  # x is a local variable because
  # it is defined inside a function.
  x = 1


# Example 2: 

  nShapes = 0
def square_area(length):
  area = length * length
  return area
def rectangle_area(width, length):
  area = width * length
  return area

# Because local variables are visible only within the function where they are defined, a programmer can define two variables with the same name as long as he defines them in different functions. In the previous example, both the square_area and rectangle_area functions contain a parameter named length and a variable named area. All four of these variables are entirely separate and do not conflict with each other in any way because the scope of each variable is local to the function where it is defined.


# When you write a program, you should use local variables whenever possible and use global variables only when absolutely necessary. Global variables (not global constants) make a program hard to understand and easy to write mistakes in the code. If you must use a global variable in your program, it is important to know that all functions can access or read the value of a global variable directly. However, in order for a function to modify the value of a global variable, the global variable must be declared as global inside the function.



# Example 3
                                    # COMMON MISTAKES
# A common mistake that many programmers make is to assume that a local variable can be used inside other functions. For example, the Python program in example 3 includes two functions named main and circle_area. The function main defines a variable named radius. Some programmers assume that the variable radius that is defined in main (and is therefore local to main only) can be used in the circle_area function. However, local variables from one function cannot be used inside another function. The local variables from main cannot be used inside circle_area.

# Example 3
import math
def main():
  radius = float(input("Enter the radius of a circle: "))
  area = circle_area()
  print(f"area: {area:.1f}")
def circle_area():
  # Mistake! There is no variable named radius
  # defined inside this function, so the variable
  # radius cannot be used in this function.
  area = math.pi * radius * radius
  return area
main()



# Example 4: 

# The correct way to fix the mistake in example 3 is to add a parameter to the circle_area function and pass the radius from the main function to the circle_area function as shown in example 4.

# Example 4
import math
def main():
  radius = float(input("Enter the radius of a circle: "))
  area = circle_area(radius)
  print(f"area: {area:.1f}")
def circle_area(radius):
  area = math.pi * radius * radius
  return area
main()



                        # Default Parameter Values and Optional Arguments
# Python allows function parameters to have default values. If a parameter has a default value, then its corresponding argument is optional. If a function is called without an argument, the corresponding parameter gets its default value.

# Consider the program in example 5. Notice at line 14 in the header for the arc_length function, that the parameter radius does not have a default value but the parameter degrees has a default value of 360. This means that when a programmer writes code to call the arc_length function, the programmer must pass a value for radius but is not required to pass a value for degrees. At line 6, the programmer wrote code to call the arc_length function and passed 4.7 for the radius parameter but did not pass a value for the degrees, so during that call to arc_length, the value of degrees will be the default value from line 14, which is 360. At line 10, the programmer wrote code to call the arc_length function again and passed two arguments: 4.7 and 270, so during that call to arc_length, the value of degrees will be 270.


# Example 5

import math
def main():
  # Call the arc_length function with only one argument
  # even though the arc_length function has two parameters.
  len1 = arc_length(4.7)
  print(f"len1: {len1:.1f}")
  # Call the arc_length function again but
  # this time with two arguments.
  len2 = arc_length(4.7, 270)
  print(f"len2: {len2:.1f}")
# Define a function with two parameters. The
# second parameter has a default value of 360.
def arc_length(radius, degrees=360):
  """Compute and return the length of an arc of a circle"""
  circumference = 2 * math.pi * radius
  length = circumference * degrees / 360
  return length
main()

                        #Function Design
# What are the properties of a good function?

# There are many things to consider when writing a function, and many authors have written about design concepts that make functions easier to understand and less error prone. 

# A good function is understandable by other programmers. One way to make a function understandable is to write a documentation string at the top of the function that describes the function, its parameters, and its return value. Another way to make a function understandable is to write comments in the body of the function as needed.
# A good function performs a single task that the programmer can describe, and the function’s name matches its task.
# A good function is relatively short, perhaps fewer than 20 lines of code.
# A good function has as few decision points (if statements and loops) as possible. Too many decision points in a function make a function error prone and difficult to test.
# A good function is as reusable as possible. Functions that use parameters and return a result are more reusable than functions that get input from a user and print results to a terminal window.


# NOTE: A variable that is defined (assigned a value) inside a function has local scope, and it can be used inside only the function where it is defined. Parameters always have local scope.

