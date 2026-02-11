import math

def main():
    height=float(input("Enter can height: "))
    radius=float(input("Enter can radius: "))
    vol=volume(radius, height)
    s_a=surface_area(radius, height)
    efficiency=vol/s_a
    print(f"the efficiency is {efficiency}")

# def storage_efficiency(volume, surface_area):



def volume(radius, height):
    radius_square= radius**2
    volume=math.pi*radius_square*height
    return volume



def surface_area(radius, height):
    radius_add_height= radius+height
    s_area= 2*math.pi*radius *radius_add_height
    return s_area

main()

