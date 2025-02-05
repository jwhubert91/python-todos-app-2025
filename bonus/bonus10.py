try:
    width = float(input("Enter a rectangle width: "))
    length = float(input("Enter a rectangle length: "))

    if width == length:
        exit("No squares allowed!")

    area = width * length
    print(f"Rectangle area is {area}")
except ValueError:
    print("Please enter a number")