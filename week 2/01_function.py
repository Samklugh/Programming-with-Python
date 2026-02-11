# this is how to define a function 

def welcome():
    """function greets user""" #docstring
    print("Welcome to my Website")

#welcome() 
#the above is how to call the function

# we can personalise the message to include username by using a parameter 


#a parameter was added in the parenthesis
def greet(name): 
    """function greets user""" #docstring
    print(f"Welcome to my Website {name}")


greet("SamOdu")  #this is used to input the arguement directly
users=input("Enter your name: ")
greet(users)  #this users a variable declared outside the function as an argument in the function
#an argument was used to provide the needed parameter.