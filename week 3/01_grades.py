

grades= float(input("Enter your grade: "))
letter_grade=""
if grades>=90:
    letter_grade="A"

elif grades>=80:
    letter_grade="B"

elif grades>=70:
    letter_grade="C"

elif grades>=60:
    letter_grade="D"

else:
    letter_grade="F"

last_digit=grades%10

sign=""
if last_digit>=7:
    sign="+"

elif last_digit<4:
    sign="-"

print(f"Your grade is {letter_grade}{sign}")

if grades>=60:
    print("Congratulations you passed!!")
else:
    print("Unfortunately, you did not pass.")

# handle exception cases

if letter_grade=="A" and sign=="+": 
    sign=""

    if letter_grade=="F":
        sign=""



# OPTION 2

# grades= float(input("Enter your grade:) "))
# letter_grade=""
# if grades>=90:
    # letter_grade="A"
# 
# elif grades>=80:
    # letter_grade="B"
# 
# elif grades>=70:
    # letter_grade="C"
# 
# elif grades>=60:
    # letter_grade="D"
# 
# else:
    # letter_grade="F"
# 
# 
# last_digito=float(str(grades)[1])
# 
# if letter_grade!="F":
    # if last_digito>=7:
        # sign="+"
    # 
    # elif last_digito<4:
        # sign="-"    
# 
    # else:
        # sign=""
# 
    # print(f"Congratulations you passed!!\nYour grade is {letter_grade}{sign}")
# 