# nested if statement

swallow= input("Choose swallow type: (fufu, garri, or semo)").strip().lower()

if swallow=="fufu":
    print("You ordered fufu")
    soup=input("please select soup: (egusi, okra, or ogbono): ").strip().lower()

    if soup=="egusi":
        print("your soup is egusi")

    elif soup=="okra":
        print("your soup is okra")

    elif soup=="ogbono":
        print("your soup is ogbono")

    else:
        print("enter correct soup choice.")



elif swallow=="garri":
    print("You ordered garri")

elif swallow=="semo":
    print("You ordered semo")

else:
    print("please enter correct option.")
