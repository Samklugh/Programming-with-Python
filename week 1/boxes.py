import math

no_of_items= float(input("Enter the number of items: "))
item_per_box= float(input("Enter the number of items per box: "))
boxes_needed= int(math.ceil(no_of_items/item_per_box))

print(f"For {(no_of_items)}, packing {item_per_box} items in each box, you will need {boxes_needed} boxes.")