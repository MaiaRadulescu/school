# Calculate area and perimeter of a shape


# Variables

shape_w = int(input("Enter  width \n"))  # shape  width
shape_l = int(input("Enter length \n"))  # shape  length


#  Function

def cal_perimeter(a, b):
    result = (a + b) * 2
    return result


def cal_area(a, b):
    result = a * b
    return result


shape_a = shape_w * shape_l  # calculate area

shape_p = (shape_l + shape_w) * 2  # calculate perimeter

if shape_w == shape_l:  # check is the shape is a square
    print(f'This is a square and area is {cal_area(shape_w, shape_l)} and perimeter is {cal_perimeter(shape_w, shape_l)}')
elif shape_w != shape_l:  # check if the shape is a rectangle
    print(f'This is a rectangle and area is {cal_area(shape_l, shape_w)} and perimeter is {cal_perimeter(shape_w, shape_l)}')
