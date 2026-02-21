import math

try:
    degree = float(input("Input degree: "))
    radian = math.radians(degree)
    print(f"Output radian: {radian:.6f}")
except ValueError:
    print("Error: Input must be a number")
print("-" * 30)

try:
    h = float(input("Height: "))
    b1 = float(input("Base, first value: "))
    b2 = float(input("Base, second value: "))
    area_trap = ((b1 + b2) / 2) * h
    print(f"Expected Output: {area_trap}")
except ValueError:
    print("Error: Inputs must be numbers")
print("-" * 30)

try:
    n_sides = int(input("Input number of sides: "))
    s_len = float(input("Input the length of a side: "))
    area_poly = (n_sides * (s_len ** 2)) / (4 * math.tan(math.pi / n_sides))
    print(f"The area of the polygon is: {int(area_poly)}") 
except ValueError:
    print("Error: Check inputs")
print("-" * 30)

try:
    base = float(input("Length of base: "))
    height = float(input("Height of parallelogram: "))
    area_para = base * height
    print(f"Expected Output: {area_para}")
except ValueError:
    print("Error: Inputs must be numbers")