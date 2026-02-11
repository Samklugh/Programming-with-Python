# age=20
# name="samson"

# # method 1:
# # print("")
# # print(f"My age is {age}")
# # print("")
# # print(f"my name is {name}")
# # print("")

# # method 2
# # print(f"""
#     #   
# # My age is {age}
# # 
# # My name is {name}
# # HAlleluja.         aement.
# # 
# # """)

# # method 3:

# # print(f"\nMy age is \n\n{age}.my name is {name}\n")
# # print(f"\nMy age is {age}.\nmy name is {name}\n")


# x=abs(-3.234322)
# # rounded_x= round(x) #round to nearest whole number
# # rounded_to_decimal_x= round(x, 3)
# # print(rounded_to_decimal_x)

# print(f" x is: {x:.5f}")


name= "samson"
surname= " odunaiya"

upper_name= name.upper() #upper case letters
lower_name= name.lower() #lower case letters
space_name_removed= surname.strip() #removes spaces before and after but not spaces between words

intro= "Hi, my name is Sam. Sam is a man. Sam lives in the UK."
count_intro=intro.count("Sam")

replace_name=intro.replace("Sam", "Mercy")

center_name= name.center(100)

endswith_intro= intro.endswith("!")
name_endswith= name.endswith("son")
name_startwith= name.startswith("Z")

intro= "Hi, my name is Sam. Sam is a man. Sam lives in the UK."
find_intro=intro.find("the")

multi_methods=surname.strip().center(120).upper().replace("ODU", "ADE")
intro2="hi, my name is mercy. mercy is a man. mercy lives in the uk."
capitalize_intro2= intro2.capitalize()

title_intro2= intro2.title()
a=("sam", "men", "God")
join_names= " ".join(a)
print(join_names)


age=20
# print(f"age is {age:-}")

