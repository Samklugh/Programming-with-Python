import math
def main():
    name="#1 picnic"
    radius=6.83
    height=10.16
    volume=can_vol(radius, height)
    area= can_area(radius, height)
    eff=volume/area
    print(f"the name is {name}, volume is {volume:.2f}, and area is {area:.2f}. The efficiency ={eff:.2f}")

    # method 2
    name="#1 Tall"
    radius=7.78
    height=11.92
    can_efficiency(name, radius, height)

    # method 3
    can_efficiency("#", 8.73, 11.59)

def can_efficiency(name, radius, height):
    volume=can_vol(radius, height)
    area=can_area(radius, height)
    efficiency=volume/area

    print(f"the name is {name}, volume is {volume:.2f}, and area is {area:.2f}. The efficiency ={efficiency:.2f}")

def can_vol(radius, height):
    volume=math.pi*radius**2*height
    return volume

def can_area(radius, height):
    area=2*math.pi*radius * (radius+height)
    return area

main()