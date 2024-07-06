from shape import Shape, Circle, Rectangle, Triangle

# Instantiating each class in a list
shapes = [Circle("yellow", 5), Rectangle("red", 4, 6), Triangle("blue", 3, 4, 5)]


# Printing out each object's name, color, area and perimeter
for shape in shapes:
    print (f'{shape.__class__.__name__} has {shape.color} color with area of {shape.calculate_area():.2f} and perimeter of {shape.calculate_perimeter():.2f}.')

# Instantiating Shape class:
new_shape = Shape("green")

# Current color for new_shape. Should print green
print(new_shape.get_color())

# Changing color of shape to purple
new_shape.set_color("purple")

# Printing new color. Should print purple
print(new_shape.get_color())