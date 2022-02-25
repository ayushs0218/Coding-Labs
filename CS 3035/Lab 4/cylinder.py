# Student Name: Ayush Singh
# CIN: 306692040
# Course: CS 3035-01
# Video Link: https://calstatela.instructuremedia.com/embed/835e7e67-9706-420a-b61a-6b974178b212

# Description: Create a constructor for the Cylinder class as well as getters/setters and str/repr functions for the object.

import math
import doctest
from shape3d import Shape3D


class Cylinder(Shape3D):
    __radius = float(1.0)
    __height = float(1.0)

    def __init__(self, radius = 1.0, height = 1.0):
        self.__radius = radius
        self.__height = height

    def get_radius(self):
        """
        Retrieve the radius value of the Cylinder object.

        Parameters
        ----------
        self : Cylinder Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        Returns
        -------
        float :
            Return the radius value of the object as a float.

        Examples
        --------
        >>> c = Cylinder(2.25, 9.8)
        >>> print(c.get_radius())
        2.25
        """
        return self.__radius

    def set_radius(self, new_radius):
        """
        Change the value of the float "radius" from what it previously was equivalent to.

        Parameters
        ----------
        self : Cylinder Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        new_radius : float
            A new float value taken in as a parameter that will replace the previous radius value.

        Returns
        -------
            None

        Examples
        --------
        >>> c = Cylinder(5.25, 6.36)
        >>> c.set_radius(9.99)
        >>> print(c.get_radius())
        9.99
        """
        self.__radius = new_radius

    def get_height(self):
        """
        Retrieve the height value of the Cylinder object.

        Parameters
        ----------
        self : Cylinder Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        Returns
        -------
        float :
            Return the height value of the object as a float.

        Examples
        --------
        >>> c = Cylinder(0.123456, 0.987654)
        >>> print(c.get_height())
        0.987654
        """
        return self.__height

    def set_height(self, new_height):
        """
        Change the value of the float "height" from what it previously was equivalent to.

        Parameters
        ----------
        self : Cylinder Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        new_height : float
            A new float value taken in as a parameter that will replace the previous height value.

        Returns
        -------
            None

        Examples
        --------
        >>> c = Cylinder(1.0, 1.0)
        >>> c.set_height(15.5)
        >>> print(c.get_height())
        15.5
        """
        self.__height = new_height

    def area(self):
        """
        Calculate and return the area of the Cylinder Object

        Parameters
        ----------
        self : Cylinder Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        Returns
        -------
        float :
            After using the values "radius" and "height" in the formula used to calculate the area of a cylinder,
            return the float value for area.

        Examples
        --------
        >>> c = Cylinder(3, 3.5)
        >>> print(c.area())
        122.52
        """
        return float(round((2 * math.pi * (self.__radius ** 2) + (2 * math.pi * self.__radius * self.__height)), 2))

    def volume(self):
        """
        Calculate and return the volume of the Cylinder Object

        Parameters
        ----------
        self : Cylinder Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        Returns
        -------
        float :
            After using the values "radius" and "height" in the formula used to calculate the volume of a cylinder,
            return the float value for volume.

        Examples
        --------
        >>> c = Cylinder(2, 2.2)
        >>> print(c.volume())
        27.65
        """
        return float(round((math.pi * (self.__radius ** 2) * self.__height), 2))

    def __str__(self):
        """
        Return a string that shows the values: "radius" and "height" of a Cylinder Object

        Parameters
        ----------
        self : Cylinder Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        Returns
        -------
        String :
            Return the values of a Cylinder Object as a string in format: Cylinder: Radius = x, Height = y

        Examples
        --------
        >>> c = Cylinder(1.5, 5.1)
        >>> print(c.__str__())
        Cylinder: Radius = 1.5, Height = 5.1
        """
        return "Cylinder: Radius = " + str(self.__radius) + ", Height = " + str(self.__height)

    def __repr__(self):
        """
        Return a string that shows the object representation of a Cylinder Object

        Parameters
        ----------
        self : Cylinder Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        Returns
        -------
        String :
            Return the string representation of a Cylinder Object in format: Cylinder(radius, height)

        Examples
        --------
        >>> c = Cylinder(99.5, 55.9)
        >>> print(c.__repr__())
        Cylinder(99.5, 55.9)
        """
        return "Cylinder(" + str(self.__radius) + ", " + str(self.__height) + ")"
