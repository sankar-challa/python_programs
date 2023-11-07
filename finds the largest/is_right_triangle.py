def is_right_triangle(side1, side2, side3):
    # Sort the sides in ascending order
    sides = sorted([side1, side2, side3])

    # Check the Pythagorean Theorem
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

# Get user input for triangle sides
side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))
side_c = float(input("Enter the length of side C: "))

# Check if it is a right triangle
if is_right_triangle(side_a, side_b, side_c):
    print("It is a right triangle.")
else:
    print("It is not a right triangle.")
