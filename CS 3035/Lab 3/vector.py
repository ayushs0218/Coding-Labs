# Student Name: Ayush Singh
# Course: CS 3035-01

# Description: Within the class "Vector" give the vector object data fields by using constructors.
# Also use operator overloading to return specific values or strings of the vector object.

class Vector:
    def __init__(self, a = 1, b = 1, c = 1):
        self.__a = a
        self.__b = b
        self.__c = c

    def __str__(self):
        """
        Return a string of the Vector Object with all of it's elements.

        Parameters
        ----------
        self : Vector Object
             An Object from class "Vector" that represents a 3D with values a, b, c.

        Returns
        -------
        String :
            Return the string of a 3D Vector in format: <a, b, c>

        Examples
        --------
        >>> v1 = Vector(5, 10, 15)
        >>> print(v1.__str__())
        <5, 10, 15>

        >>> v2 = Vector()
        >>> print(v2)
        <1, 1, 1>
        """
        return "<" + str(self.__a) + ", " + str(self.__b) + ", " + str(self.__c) + ">"

    # __repr__()
    def __repr__(self):
        """
        Return a string representation of the Vector Object with all of it's elements.

        Parameters
        ----------
        self : Vector Object
             An Object from class "Vector" that represents a 3D with values a, b, c.

        Returns
        -------
        String :
            Return the string representation of a 3D Vector in format: Vector(a, b, c)

        Examples
        --------
        >>> v1 = Vector(10, 100, 1000)
        >>> print(v1.__repr__())
        Vector(10, 100, 1000)
        """
        return "Vector(" + str(self.__a) + ", " + str(self.__b) + ", " + str(self.__c) + ")"

    # magnitude()
    def magnitude(self):
        """
            Return an integer value of the magnitude of the 3D Vector.
            The magnitude is calculated by finding the sum of all the squared
            values of the 3D Vector (a, b, c).

            Parameters
            ----------
            self : Vector Object
            An Object from class "Vector" that represents a 3D with values a, b, c.

            Returns
            -------
            int :
                Return the magnitude of a 3D Vector

            Examples
            --------
            >>> v1 = Vector(1, 2, 2)
            >>> print(v1.magnitude())
            3.0
        """

        sum = (self.__a ** 2) + (self.__b ** 2) + (self.__c ** 2)
        return sum ** .5

    # == operand operator overload
    def __eq__(self, other):
        """
            Return a boolean value if the two parameters (Vector Objects) are equivalent to each other.

            Parameters
            ----------
            self : Vector Object
                An Object from class "Vector" that represents a 3D Vector with values a, b, c.

            other : Vector Object
                An Object from class "Vector" that represents a 3D Vector with values a, b, c.

            Returns
            -------
            Boolean :
                Return Boolean value True if the vectors are equivalent, false otherwise.

            Examples
            --------
            >>> v1 = Vector(10, 100, 1000)
            >>> v2 = Vector(10, 100, 1000)
            >>> print(v1 == v2)
            True
            >>> v1 = Vector(10, 100, 1000)
            >>> v3 = Vector(1, 2, 3)
            >>> print(v1 == v3)
            False
        """

        if self.__a == other.__a and self.__b == other.__b and self.__c == other.__c:
            return True
        else:
            return False

    # + and += operator overload
    def __add__(self, other):
        """
            Return a new Vector Object that represents the sum of two vectors.

            Parameters
            ----------
            self : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            other : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            Returns
            -------
            Vector Object :
                Return a Vector object that represents the sum between two 3D Vectors.

            Examples
            --------
            >>> v1 = Vector(1, 10, 100)
            >>> v2 = Vector(5, 50, 500)
            >>> print(v1 + v2)
            <6, 60, 600>
        """

        return Vector((self.__a + other.__a), (self.__b + other.__b), (self.__c + other.__c))

    def __iadd__(self, other):
        """
            Return an updated version of the 'self' Vector Object that represents the sum of two vectors.

            Parameters
            ----------
            self : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            other : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            Returns
            -------
            Vector Object :
                Return an updated form of the 'self' Vector Object that contains the sum of the two vectors

            Examples
            --------
            >>> v1 = Vector(1, 2, 3)
            >>> v2 = Vector(4, 5, 7)
            >>> v1 += v2
            >>> print(v1)
            <5, 7, 10>
        """

        self.__a += other.__a
        self.__b += other.__b
        self.__c += other.__c
        return self

    # - and -+ operator overload
    def __sub__(self, other):
        """
            Return a new Vector Object that represents the difference of two vectors.

            Parameters
            ----------
            self : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            other : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            Returns
            -------
            Vector Object :
                Return a Vector object that represents the difference between two 3D Vectors.

            Examples
            --------
            >>> v1 = Vector(5000, 10000, 5000)
            >>> v2 = Vector(300, 700, 500)
            >>> print(v1 - v2)
            <4700, 9300, 4500>
        """

        return Vector((self.__a - other.__a), (self.__b - other.__b), (self.__c - other.__c))

    def __isub__(self, other):
        """
            Return an updated version of the 'self' Vector Object that represents the difference of two vectors.

            Parameters
            ----------
            self : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            other : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            Returns
            -------
            Vector Object :
                Return an updated form of the 'self' Vector Object that contains the difference of the two vectors

            Examples
            --------
            >>> v1 = Vector(20, 35, 50)
            >>> v2 = Vector(11, 22, 33)
            >>> v1 -= v2
            >>> print(v1)
            <9, 13, 17>
        """

        self.__a -= other.__a
        self.__b -= other.__b
        self.__c -= other.__c
        return self

    # * and *= operator overload
    def __mul__(self, other):
        """
            Return a new Vector Object that represents either the dot product if both parameters are vectors or
            scalar multiplication if the 'other' parameter is an integer value.

            Parameters
            ----------
            self : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            other : Vector Object (expected type of other)
                An Object from class "Vector" that represents a 3D with values a, b, c.

            other : int
                An integer value that represents the value to multiply the vector for Scalar Nultiplication

            Returns
            -------
            int (expected) :
                Return an integer value that represents the dot product of two vectors.

            Vector Object :
                Return a new Vector Object that represents the Scalar Multiplication product
                between a Vector and an Integer

            Examples
            --------
            >>> v1 = Vector(1, 20, 40)
            >>> v2 = Vector(5, 4, 2)
            >>> print(v1 * v2)
            72

            >>> v1 = Vector(1, 2, 3)
            >>> print(v1 * 5)
            <5, 10, 15>
        """
        if isinstance(other, int) and isinstance(self, Vector):
            return Vector((self.__a * other), (self.__b * other), (self.__c * other))
        else:
            return (self.__a + other.__a) + (self.__b + other.__b) + (self.__c + other.__c)

    # Added __rmul__ in order to handle cases where Scalar Multiplication is in form: int * Vector
    def __rmul__(self, other):
        """
            If the self value is an int and the "other" value is a vector then perform Scalar Multiplication

            Parameters
            ----------
            self : int
                An Object from class "Vector" that represents a 3D with values a, b, c.

            other : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            Returns
            -------
            Vector Object :
                Return a new Vector Object that represents the Scalar Multiplication product
                between a Vector and an Integer

            Examples
            --------
            >>> v1 = Vector(1, 2, 3)
            >>> print(5 * v1)
            <5, 10, 15>

            >>> v1 = Vector(1, 1, 1)
            >>> print(9 * v1)
            <9, 9, 9>
        """
        if isinstance(other, Vector) and isinstance(self, int):
            return Vector((self * other.__a), (self * other.__b), (self * other.__c))
        elif isinstance(other, int) and isinstance(self, Vector):
            return Vector((self.__a * other), (self.__b * other), (self.__c * other))

    def __imul__(self, other):
        """
            Return an updated version of the 'self' Vector Object that represents the product of a vector and integer.

            Parameters
            ----------
            self : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            other : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            Returns
            -------
            Vector Object :
                Return an updated form of the 'self' Vector Object that contains the product of the two vectors

            Examples
            --------
            >>> v1 = Vector(20, 35, 50)
            >>> v1 *= 2
            >>> print(v1)
            <40, 70, 100>
        """

        self.__a *= other
        self.__b *= other
        self.__c *= other
        return self

    # % operator overload
    def __mod__(self, other):
        """
            Return an updated version of the 'self' Vector Object that represents cross product between two vectors.

            Parameters
            ----------
            self : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            other : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            Returns
            -------
            Vector Object :
                Return a new Vector Object that represents the Cross Product of two vectors

            Examples
            --------
            >>> v1 = Vector(20, 35, 50)
            >>> v2 = Vector(1, 2, 3)
            >>> print(v1 % v2)
            <5, -10, 5>
        """

        value_a = (self.__b * other.__c) - (self.__c * other.__b)
        value_b = (self.__c * other.__a) - (self.__a * other.__c)
        value_c = (self.__a * other.__b) - (self.__b * other.__a)
        return Vector(value_a, value_b, value_c)

    # [] operator overload
    def __getitem__(self, item):
        """
            Return specific elements of the 'self' vector. (a, b, c)

            Parameters
            ----------
            self : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            item : int
                An integer value that represents the position for which value should be received in the vector.

            Returns
            -------
            int :
                Return a specific element of the 'self' vector. (a, b, c)

            Examples
            --------
            >>> v1 = Vector(5, 10, 15)
            >>> print("a value: " + str(v1[0]))
            a value: 5

            >>> v1 = Vector(5, 10, 15)
            >>> print("b value: " + str(v1[1]))
            b value: 10

            >>> v1 = Vector(5, 10, 15)
            >>> print("c value: " + str(v1[2]))
            c value: 15
        """

        if item == 0:
            return self.__a
        elif item == 1:
            return self.__b
        elif item == 2:
            return self.__c

    def __setitem__(self, key, value):
        """
            Alter a value within the 'self' vector.

            Parameters
            ----------
            self : Vector Object
                An Object from class "Vector" that represents a 3D with values a, b, c.

            key : int
                An integer value that represents the position for which value should be changed in the vector.

            value: int
                An integer value that will be used to replace the previous value within the vector that will be altered.

            Examples
            --------
            >>> v1 = Vector(5, 10, 15)
            >>> v1[0] = 0
            >>> print(v1)
            <0, 10, 15>

            >>> v1 = Vector(5, 10, 15)
            >>> v1[1] = 0
            >>> print(v1)
            <5, 0, 15>

            >>> v1 = Vector(5, 10, 15)
            >>> v1[2] = 0
            >>> print(v1)
            <5, 10, 0>
        """

        if key == 0:
            self.__a = value
        elif key == 1:
            self.__b = value
        elif key == 2:
            self.__c = value



import doctest
print(doctest.testmod())
