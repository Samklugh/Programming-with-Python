from datetime import datetime

discounnt_rate=0.1
tax_rate= 0.06
today= datetime.now()
day_of_week=today.weekday()

subtotal=0
quantity=1
while quantity !=0:
    quantity= int(input("Enter quantity: "))
    if quantity !=0:
        price= float(input("Enter price: "))
        subtotal +=price

print(f"subtotal {subtotal:.2f}")
discount=0
if day_of_week==2 or day_of_week==3: #or if day_of_week in [2,3] since week days are 0 for sunday, 1 for monday etc according to the pythn date time documentation
    if subtotal>50:
        discount=round(subtotal * discounnt_rate, 2)
        print(f"discount {discount:.2f}")
    else:
        short=50-subtotal
        print(f"You can get a discount by ordering {short:.2f} more.")

subtotal -=discount
tax= round(subtotal * tax_rate, 2)
total= subtotal + tax
print(f"tax {tax:.2f}")
print(f"Total Due {total}")