# Student Name: Ayush Singh
# CIN: 306692040
# Course: CS 3035-01
# Video Link: https://calstatela.instructuremedia.com/embed/835e7e67-9706-420a-b61a-6b974178b212

# Description: An abstract class that will have abstract methods for the Pyramid and Cylinder Classes.
from abc import ABC, abstractmethod


class Shape3D(ABC):
    __color = str("black")
    __transparency = float(0.0)

    def __init__(self, color = "black", transparency = 0.0):
        self.__color = color
        self.__transparency = transparency

    def get_color(self):
        """
        Retrieve the color value of the Shape3D object.

        Parameters
        ----------
        self : Shape3D Object
            An object that represents a basic 3D with values "color" and "transparency" as parameters

        Returns
        -------
        String :
            Return the color value of a Shape3D Object as a String.
        """
        return self.__color

    def set_color(self, new_color):
        """
        Change the value of the String "color" from what it previously was equivalent to.

        Parameters
        ----------
        self : Shape3D Object
            An object that represents a basic 3D with values "color" and "transparency" as parameters

        new_color : float
            A new String value taken in as a parameter that will replace the previous color value.

        Returns
        -------
            None
        """
        self.__color = new_color

    def get_transparency(self):
        """
        Retrieve the transparency value of the Shape3D object.

        Parameters
        ----------
        self : Shape3D Object
            An object that represents a basic 3D with values "color" and "transparency" as parameters

        Returns
        -------
        float :
            Return the transparency value of a Shape3D Object as a float.

        """
        return self.__transparency

    def set_transparency(self, new_transparency):
        """
        Change the value of the float "transparency" from what it previously was equivalent to.

        Parameters
        ----------
        self : Shape3D Object
            An object that represents a basic 3D with values "color" and "transparency" as parameters

        new_transparency : float
            A new float value taken in as a parameter that will replace the previous transparency value.

        Returns
        -------
            None
        """
        self.__transparency = new_transparency

    @abstractmethod
    def area(self):
        """
        Create an abstract method "area()" that will be inherited by the subclasses to Shape3D(ABC). Subclasses will
        individually define their own area() methods.

        Parameters
        ----------
        self : Shape3D Object
            An object that represents a basic 3D with values "color" and "transparency" as parameters

        Returns
        -------
        None

        """
        pass

    @abstractmethod
    def volume(self):
        """
        Create an abstract method "volume()" that will be inherited by the subclasses to Shape3D(ABC). Subclasses will
        individually define their own volume() methods.

        Parameters
        ----------
        self : Shape3D Object
            An object that represents a basic 3D with values "color" and "transparency" as parameters

        Returns
        -------
        None

        """
        pass

    def __str__(self):
        """
        Return a string that shows the values: "color" and "transparency" of a Shape3D Object

        Parameters
        ----------
        self : Shape3D Object
            An object that represents a cylinder with values "color" and "transparency" as parameters

        Returns
        -------
        String :
            Return the values of a Shape3D Object as a string in format: Shape Color: color, Shape Transparency: transparency
        """
        return "Shape Color: " + self.__color + ", Shape Transparency: " + str(self.__transparency)

    def __repr__(self):
        """
        Return a string that shows the object representation of a Shape3D Object

        Parameters
        ----------
        self : Shape3D Object
            An object that represents a cylinder with values "color" and "transparency" as parameters

        Returns
        -------
        String :
            Return the string representation of a Shape3D Object in format: Shape3D(color, transparency)


        """
        return "Shape3D(" + self.__color + ", " + str(self.__transparency) +")"

