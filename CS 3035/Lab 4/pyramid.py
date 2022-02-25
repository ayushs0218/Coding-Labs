# Student Name: Ayush Singh
# CIN: 306692040
# Course: CS 3035-01
# Video Link: https://calstatela.instructuremedia.com/embed/835e7e67-9706-420a-b61a-6b974178b212

# Description: Create a constructor for the Pyramid class as well as getters/setters and str/repr functions for the object.

from shape3d import Shape3D


class Pyramid(Shape3D):

    __base = float(1.0)
    __height = float(1.0)
    __slant = float(1.0)

    def __init__(self, base = 1.0, height = 1.0, slant = 1.0):
        self.__base = base
        self.__height = height
        self.__slant = slant

    def get_base(self):
        """
        Retrieve the base value of the Pyramid object.

        Parameters
        ----------
        self : Pyramid Object
            An object that represents a cylinder with values "base", "height", and "slant" as parameters

        Returns
        -------
        float :
            Return the base value of the object as a float.

        Examples
        --------
        >>> p = Pyramid(13.3, 15.5, 19)
        >>> print(p.get_base())
        13.3
        """
        return self.__base

    def set_base(self, new_base):
        """
        Change the value of the float "base" from what it previously was equivalent to.

        Parameters
        ----------
        self : Pyramid Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        new_base : float
            A new float value taken in as a parameter that will replace the previous radius value.

        Returns
        -------
            None

        Examples
        --------
        >>> p = Pyramid(0,0,0)
        >>> p.set_base(99.9)
        >>> print(p.get_base())
        99.9
        """
        self.__base = new_base

    def get_height(self):
        """
        Retrieve the height value of the Pyramid object.

        Parameters
        ----------
        self : Pyramid Object
            An object that represents a cylinder with values "base", "height", and "slant" as parameters

        Returns
        -------
        float :
            Return the height value of the object as a float.

        Examples
        --------
        >>> p = Pyramid(1,2,3)
        >>> print(p.get_height())
        2.0
        """
        return float(self.__height)

    def set_height(self, new_height):
        """
        Change the value of the float "height" from what it previously was equivalent to.

        Parameters
        ----------
        self : Pyramid Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        new_height : float
            A new float value taken in as a parameter that will replace the previous radius value.

        Returns
        -------
            None

        Examples
        --------
        >>> p = Pyramid(3,3,3)
        >>> p.set_height(6.0)
        >>> print(p.get_height())
        6.0
        """
        self.__height = new_height

    def get_slant(self):
        """
        Retrieve the slant value of the Pyramid object.

        Parameters
        ----------
        self : Pyramid Object
            An object that represents a cylinder with values "base", "height", and "slant" as parameters

        Returns
        -------
        float :
            Return the slant value of the object as a float.

        Examples
        --------
        >>> p = Pyramid(0,0,1)
        >>> print(p.get_slant())
        1.0
        """
        return float(self.__slant)

    def set_slant(self, new_slant):
        """
        Change the value of the float "slant" from what it previously was equivalent to.

        Parameters
        ----------
        self : Pyramid Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        new_slant : float
            A new float value taken in as a parameter that will replace the previous radius value.

        Returns
        -------
            None

        Examples
        --------
        >>> p = Pyramid(1,10,1000)
        >>> p.set_slant(100)
        >>> p.get_slant()
        100.0

        """
        self.__slant = new_slant

    def area(self):
        """
        Calculate and return the area of the Pyramid Object

        Parameters
        ----------
        self : Pyramid Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        Returns
        -------
        float :
            After using the values "base", "height", and "slant" in the formula used to calculate the area of a
            cylinder, return the float value for area.

        Examples
        --------
        >>> p = Pyramid(5, 10, 15)
        >>> print(p.area())
        175.0
        """
        return float(round((2 * self.__base * self.__slant) + (self.__base ** 2), 2))

    def volume(self):
        """
        Calculate and return the volume of the Pyramid Object

        Parameters
        ----------
        self : Pyramid Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        Returns
        -------
        float :
            After using the values "base" and "height" in the formula used to calculate the volume of a cylinder,
            return the float value for volume.

        Examples
        --------
        >>> p = Pyramid(15, 10, 5)
        >>> print(p.volume())
        750.0
        """
        return round((1/3) * (self.__base ** 2) * self.__height, 2)

    def __str__(self):
        """
        Return a string that shows the values: "base", "height", and "slant" of a Pyramid Object

        Parameters
        ----------
        self : Pyramid Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        Returns
        -------
        String :
            Return the values of a Pyramid Object as a string in format: Pyramid: base = x, Height = y, Slant = z

        Examples
        --------
        >>> p = Pyramid(10,10,10)
        >>> print(p.__str__())
        Pyramid: Base = 10, Height = 10, Slant = 10
        """
        return "Pyramid: Base = " + str(self.__base) + ", Height = " + str(self.__height) + ", Slant = " + str(self.__slant)

    def __repr__(self):
        """
        Return a string that shows the object representation of a Pyramid Object

        Parameters
        ----------
        self : Pyramid Object
            An object that represents a cylinder with values "radius" and "height" as parameters

        Returns
        -------
        String :
            Return the string representation of a Pyramid Object in format: Pyramid(base, height, slant)

        Examples
        --------
        >>> p = Pyramid(11, 22, 22)
        >>> print(p.__repr__())
        Pyramid(11, 22, 22)
        """
        return "Pyramid(" + str(self.__base) + ", " + str(self.__height) + ", " + str(self.__slant) + ")"
