# Calculate area of a shape


# Variables

shape_w = int(input("Enter  width \n"))  # rectangle width
shape_h = int(input("Enter height \n"))  # rectangle height

shape_a = shape_w * shape_h  # calculate area

shape_p = (shape_h + shape_w) * 2 # calculate perimeter

if shape_w == shape_h:
    print(f'This is a square and area is {shape_a}')
elif shape_w != shape_h:
    print(f'This is a rectangle and are is {shape_a}')
