feet_inches = input("Enter feet and inches: ")

def parse(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    feet = float(parts[0])
    inches = float(parts[1]) + feet * 12
    return inches

def convert_inches_to_meters(inches):
    meters = inches * 0.0254
    return meters

inches_global = parse(feet_inches)
result = convert_inches_to_meters(inches_global)

if result < 1:
    print("Kid is too short")
else:
    print("Kid can use the slide")