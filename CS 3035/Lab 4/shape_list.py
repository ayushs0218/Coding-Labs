# Student Name: Ayush Singh
# CIN: 306692040
# Course: CS 3035-01
# Video Link: https://calstatela.instructuremedia.com/embed/835e7e67-9706-420a-b61a-6b974178b212

# Description: Create a constructor for the ShapeList class as well as functions that calculate various values of the
# with the objects in the ShapeList.

from cylinder import Cylinder
from pyramid import Pyramid


class ShapeList(list):
    def __init__(self, list_parameter):
        list.__init__(self, list_parameter)

    def average_area_of_cylinders(self):
        """
        Traverse through a list of 3D Shapes (containing either Cylinder or Pyramid objects). When a Cylinder object is
        found in the list accumulate all the cylinder areas values in a single variable then, divide by the number of
        cylinders in order to get the average area of all cylinders in the list.

        Parameters
        ----------
        self : ShapeList list
            A list that contains both Cylinder objects and Pyramid objects

        Returns
        -------
        float :
            Return a float value that is equivalent to the average area of all cylinders in a list.

        Examples
        --------
        >>> s = ShapeList([])
        >>> c1 = Cylinder(1,2)
        >>> s.append(c1)
        >>> p1 = Pyramid(1,2,3)
        >>> s.append(p1)
        >>> c2 = Cylinder(3,4)
        >>> s.append(c2)
        >>> p2 = Pyramid(4,5,6)
        >>> s.append(p2)
        >>> print(s.average_area_of_cylinders())
        75.4
        """

        area_total = 0
        cylinder_count = 0
        for i in range(len(self)):
            if isinstance(self[i], Cylinder):
                cylinder_count += 1
                area_total = area_total + self[i].area()
        area_average = area_total / cylinder_count
        return round(area_average, 2)

    def average_area_of_pyramids(self):
        """
        Traverse through a list of 3D Shapes (containing either Cylinder or Pyramid objects). When a Pyramid object is
        found in the list accumulate all the pyramid areas values in a single variable then, divide by the number of
        pyramids in order to get the average area of all pyramids in the list.

        Parameters
        ----------
        self : ShapeList list
            A list that contains both Cylinder objects and Pyramid objects

        Returns
        -------
        float :
            Return a float value that is equivalent to the average area of all pyramids in a list.

        Examples
        --------
        >>> s = ShapeList([])
        >>> c1 = Cylinder(1,2)
        >>> s.append(c1)
        >>> p1 = Pyramid(1,2,3)
        >>> s.append(p1)
        >>> c2 = Cylinder(3,4)
        >>> s.append(c2)
        >>> p2 = Pyramid(4,5,6)
        >>> s.append(p2)
        >>> print(s.average_area_of_pyramids())
        35.5
        """
        area_total = 0
        pyramid_count = 0
        for i in range(len(self)):
            if isinstance(self[i], Pyramid):
                pyramid_count += 1
                area_total = area_total + self[i].area()
        area_total = area_total / pyramid_count
        return round(area_total, 2)

    def max_volume(self):
        """
        Traverse through a list that contains 3D shapes (Cylinder and Pyramid Objects). When the volume of a certain
        object in the list is greater than the reference variable (initial value = Position 0 Volume - 1), then replace
        the value of the reference variable to the current volume and store the object at the index of the for loop.
        When the whole list is traversed, return the object with the biggest volume.

        Parameters
        ----------
        self : ShapeList list
            A list that contains both Cylinder objects and Pyramid objects

        Returns
        -------
        Shape3D Object
            Return a Shape3D object that contains the biggest volume of all objects in the list.

        Examples
        --------
        >>> s = ShapeList([])
        >>> c1 = Cylinder(1,2)
        >>> s.append(c1)
        >>> p1 = Pyramid(1,2,3)
        >>> s.append(p1)
        >>> c2 = Cylinder(3,4)
        >>> s.append(c2)
        >>> p2 = Pyramid(4,5,6)
        >>> s.append(p2)
        >>> print(s.max_volume())
        Cylinder: Radius = 3, Height = 4
        """

        max_volume = self[0].volume() - 1
        for i in range(len(self)):
            if self[i].volume() > max_volume:
                max_volume = self[i].volume()
                max_value_object = self[i]
        return max_value_object

    def min_volume(self):
        """
        Traverse through a list that contains 3D shapes (Cylinder and Pyramid Objects). When the volume of a certain
        object in the list is less than the reference variable (initial value = Position 0 Volume + 1), then replace the
        value of the reference variable to the current volume and store the object at the index of the for loop. When the
        whole list is traversed, return the object with the smallest volume.

        Parameters
        ----------
        self : ShapeList list
            A list that contains both Cylinder objects and Pyramid objects

        Returns
        -------
        Shape3D Object
            Return a Shape3D object that contains the smallest volume of all objects in the list.

        Examples
        --------
        >>> s = ShapeList([])
        >>> c1 = Cylinder(1,2)
        >>> s.append(c1)
        >>> p1 = Pyramid(1,2,3)
        >>> s.append(p1)
        >>> c2 = Cylinder(3,4)
        >>> s.append(c2)
        >>> p2 = Pyramid(4,5,6)
        >>> s.append(p2)
        >>> print(s.min_volume())
        Pyramid: Base = 1, Height = 2, Slant = 3
        """
        min_volume = self[0].volume() + 1
        for i in range(len(self)):
            if self[i].volume() < min_volume:
                min_volume = self[i].volume()
                min_volume_object = self[i]
        return min_volume_object

    def display_cylinders(self):
        """
        Traverse through a list of 3D shapes (containing both Cylinder and Pyramid Objects). If the current object in
        the traversal is a Cylinder, then add the Cylinder Object to a new list. After the traversal of the list,
        return the list of Cylinder Objects.

        Parameters
        ----------
        self : ShapeList list
            A list that contains both Cylinder objects and Pyramid objects

        Returns
        -------
        list :
            Return a list that solely contains the Cylinder Objects from the original list

        Examples
        --------
        >>> s = ShapeList([])
        >>> c1 = Cylinder(1,2)
        >>> s.append(c1)
        >>> p1 = Pyramid(2,3,4)
        >>> s.append(p1)
        >>> c2 = Cylinder(3,4)
        >>> s.append(c2)
        >>> p2 = Pyramid(4,5,6)
        >>> s.append(p2)
        >>> print(s.display_cylinders())
        [Cylinder(1, 2), Cylinder(3, 4)]

        """
        cylinders = []
        for i in range(len(self)):
            if isinstance(self[i], Cylinder):
                cylinders.append(self[i])
        return cylinders

    def display_pyramids(self):
        """
        Traverse through a list of 3D shapes (containing both Cylinder and Pyramid Objects). If the current object in
        the traversal is a Pyramid, then add the Pyramid Object to a new list. After the traversal of the list,
        return the list of Pyramid Objects.

        Parameters
        ----------
        self : ShapeList list
            A list that contains both Cylinder objects and Pyramid objects

        Returns
        -------
        list :
            Return a list that solely contains the Pyramid Objects from the original list

        Examples
        --------
        >>> s = ShapeList([])
        >>> c1 = Cylinder(1,2)
        >>> s.append(c1)
        >>> p1 = Pyramid(1,2,3)
        >>> s.append(p1)
        >>> c2 = Cylinder(3,4)
        >>> s.append(c2)
        >>> p2 = Pyramid(4,5,6)
        >>> s.append(p2)
        >>> print(s.display_pyramids())
        [Pyramid(1, 2, 3), Pyramid(4, 5, 6)]
        """
        pyramids = []
        for i in range(len(self)):
            if isinstance(self[i], Pyramid):
                pyramids.append(self[i])
        return pyramids
