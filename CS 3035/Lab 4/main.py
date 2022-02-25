# Student Name: Ayush Singh
# CIN: 306692040
# Course: CS 3035-01
# Video Link: https://calstatela.instructuremedia.com/embed/835e7e67-9706-420a-b61a-6b974178b212

# Description: Import the classes from the other modules and ask the user for how many objects (Cylinder/Pyramids)
# should be created. Print out values of the 3D Shapes (Objects) and ShapeList accordingly.

from cylinder import Cylinder
from pyramid import Pyramid
from shape_list import ShapeList
import random


def main():
    color_list = [
        "red", "green", "yellow", "orange", "blue", "pink", "purple", "black", "white", "brown",
        "violet", "turquoise", "maroon", "gray", "cyan", "crimson", "gold", "bronze", "silver", "magenta"]

    shape_list = ShapeList([])

    cylinders = int(input("How Many Cylinders Do You Want: "))
    pyramids = int(input("How Many Pyramids Do You Want: "))
    print("")

    print("-----------------------------------------------------------------")
    for c in range(cylinders):
        print("Cylinder " + str(c + 1) + ":")
        radius = round(random.uniform(0.00, 50.00), 2)
        height = round(random.uniform(0.00, 50.00), 2)
        transparency = round(random.uniform(0.00, 1.00), 2)
        random_color = random.randint(0, 19)

        cylinder = Cylinder(radius, height)
        cylinder.set_color(color_list[random_color])
        cylinder.set_transparency(transparency)
        shape_list.append(cylinder)

        print("__str__(): " + cylinder.__str__())
        print("__repr__(): " + cylinder.__repr__())
        print("Transparency: " + str(cylinder.get_transparency()))
        print("Color: " + str(cylinder.get_color()))
        print("Area: " + str(cylinder.area()))
        print("Volume: " + str(cylinder.volume()))
        print("")
    print("-----------------------------------------------------------------")

    for p in range(pyramids):
        print("Pyramid " + str(p + 1) + ":")
        base = round(random.uniform(0.00, 50.00), 2)
        height = round(random.uniform(0.00, 50.00), 2)
        slant = round(random.uniform(0.00, 50.00), 2)
        transparency = round(random.uniform(0.00, 1.00), 2)
        random_color = random.randint(0, 19)

        pyramid = Pyramid(base, height, slant)
        pyramid.set_color(color_list[random_color])
        pyramid.set_transparency(transparency)
        shape_list.append(pyramid)

        print("__str__(): " + pyramid.__str__())
        print("__repr__(): " + pyramid.__repr__())
        print("Transparency: " + str(pyramid.get_transparency()))
        print("Color: " + str(pyramid.get_color()))
        print("Area: " + str(pyramid.area()))
        print("Volume: " + str(pyramid.volume()))
        print("")

    print("-----------------------------------------------------------------")
    print("")
    random.shuffle(shape_list)
    print("Randomized List: " + str(shape_list))
    print("Average Area Of Cylinders: " + str(shape_list.average_area_of_cylinders()))
    print("Average Area Of Pyramids: " + str(shape_list.average_area_of_pyramids()))
    print("Max Volume 3D Shape: " + str(shape_list.max_volume()))
    print("Max Volume Value: " + str(shape_list.max_volume().volume()))
    print("Min Volume 3D Shape: " + str(shape_list.min_volume()))
    print("Min Volume Value: " + str(shape_list.min_volume().volume()))

    print("Cylinders: " + str(shape_list.display_cylinders()))
    print("Pyramids: " + str(shape_list.display_pyramids()))


if __name__ == '__main__':
    main()
