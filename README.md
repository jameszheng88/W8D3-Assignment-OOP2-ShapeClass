# W8D3-Assignment-OOP2-ShapeClassHierarchy

## Overview
This document outlines the implementation of a shape class hierachy in Python. The base class is "Shape", and it has 3 subclasses: "Circle", "Rectangle", and "Triangle". Each subclass provides specific implementations for calculating the are and perimeter. There are 2 files in the project. "shape.py" define the class and subclasses, while "main.py" demonstrates creating shapes, calculating their areas and perimeters, and changing colors.

## Classes

### Base Class: Shape
The "Shape" class is a base class that includes basic properties and methods shared by all shapes.

#### Attributes
- **color**: The color of the shape.
  
#### Methods
- **__init__(self, color)**: Initializes the shape with a given color
- **calculate_area(self)**: Returns "None". This method is meant to be overridden by subclasses.
- **calculate_perimeter(self)**: Returns "None". This method is meant to be overridden by subclasses.
- **get_color(self)**: Returns the color of the shape.
- **set_color(self, color)**: Sets the color of the shape.
  
### Subclass: Circle
The "Circle" class inherits from "Shape" and provides implementations for calculating the area and perimeter. 

#### Attributes
- **color**: The color of the circle.
- **radius**: The radius of the circle.

#### Methods
- **__init__(self, color, radius)**: Initializes the circle with a color and radius.
- **calculate_area(self)**: Calculates and returns the area of the circle.
- **calculate_perimeter(self)**: Calculates and returns the perimeter (circumference) of the circle.

### Subclass: Rectangle
The "Rectangle" class inherits from "Shape" and provides specific implementations for calculating the area and perimeter.

#### Attributes
- **color**: The color of the rectangle.
- **length**: The length of the rectangle.
- **width**: The width of the rectangle.

#### Methods
- **__init__(self, color, length, width)**: Initializes the rectangle with a color, length, and width.
- **calculate_area(self)**: Calculates and returns the area of the rectangle.
- **calculate_perimeter(self)**: Calculates and returns the perimeter of the rectangle.

### Subclass: Triangle
The "Triangle" class inherits from "Shape" and provides specific implementations for calculating the area and perimeter.

#### Attributes
- **color**: The color of the triangle.
- **side1**: The length of the first side.
- **side2**: The width of the second side.
- **side3**: The width of the third side.

#### Methods
- **__init__(self, color, side1, side2, side3)**: Initializes the triangle with a color and the lengths of its three sides.
- **calculate_area(self)**: Calculates and returns the area of the triangle using Heron's formula.
- **calculate_perimeter(self)**: Calculates and returns the perimeter of the triangle.

## Main.py
This file demonstrates the usage of the classes defined in "shape.py". It creates instances of each shape, calculates their areas and perimeters, and prints the results. Additionally, it shows how to change the color of the shape.

## Dependencies
Python standard library (math module)








