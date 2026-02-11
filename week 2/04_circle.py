# A function is a group of statements that together perform one task. Broadly speaking, there are four types of functions in Python which are:

# Built-in functions
# Standard library functions
# Third-party functions
# User-defined functions

# A user-defined function is a function that is not a built-in function, a standard function, or a third-party function. A user-defined function is written by a programmer like yourself as part of a program. For some students the term “user-defined function” is confusing because the user of a program doesn’t define the function. Instead, the programmer (you) define user-defined functions. Perhaps a more correct term is programmer-defined function. Writing user-defined functions has several advantages, including:
# 
# making your code more reusable
# making your code easier to understand and debug
# making your code easier to change and add capabilities

def circle (x, y, radiu):
    """This function gives the area of a circle"""
    length=x
    height=y
    radius=radiu
    area=x*y*radius
    return area

print(circle(3, 6, 12))