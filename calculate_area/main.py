# Calculate area and perimeter of a shape


# Variables

shape_w = int(input("Enter  width \n"))  # shape  width
shape_l = int(input("Enter length \n"))  # shape  length

shape_a = shape_w * shape_l  # calculate area

shape_p = (shape_l + shape_w) * 2  # calculate perimeter

if shape_w == shape_l:  # check is the shape is a square
    print(f'This is a square and area is {shape_a} and perimeter is {shape_p}')
elif shape_w != shape_l:  # check if the shape is a rectangle
    print(f'This is a rectangle and area is {shape_a} and perimeter is {shape_p}')
