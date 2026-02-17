def get_positive_values (prompt_text):
    """Prompt the user for a value and re-prompt them if the value is negative"""

    # Step 1: prompt for the value from user 
    value=float(input(prompt_text))


    # step 2: check if the value is positive and reprompt if negative
    while value<0:
        print("sorry, value must be positive")
        value=float(input(prompt_text))

    #step 3: return the value 
    return value




# length=float(input("Enter the length: "))
# width=float(input("Enter the width: "))

# the below code can be used for length and width using the function that ensures that only positive number is entered
length=get_positive_values("enter the length")
width=get_positive_values("enter the width")
area= length*width
print (f"\nthe area is {area}\n")